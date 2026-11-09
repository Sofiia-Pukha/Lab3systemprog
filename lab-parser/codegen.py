# Генерація коду: трансляція AST у програму на Python
import keyword

from interpreter import SemanticError

PY_NAMES = {'print', 'int', 'float', 'bool', 'math'}
COMPARE = {'<', '>', '<=', '>=', '==', '!='}


class CodeGen:
    def __init__(self):
        self.lines = []
        self.level = 0
        # стек областей видимості: ім'я -> тип (для семантичної перевірки)
        self.scopes = [{}]

    def generate(self, tree):
        self.emit('# Код згенеровано транслятором з підмножини мови C')
        self.emit('import math')
        self.emit('')
        for st in tree.children:
            self.stmt(st)
        return '\n'.join(self.lines) + '\n'

    def emit(self, text):
        self.lines.append('    ' * self.level + text)

    def py_name(self, name):
        # якщо ім'я змінної збігається зі словом Python, додаємо _
        if keyword.iskeyword(name) or name in PY_NAMES:
            return name + '_'
        return name

    def lookup(self, name, line):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise SemanticError(f"Рядок {line}: змінна '{name}' не оголошена")

    def body(self, n):
        self.level += 1
        start = len(self.lines)
        self.stmt(n)
        if len(self.lines) == start:
            self.emit('pass')
        self.level -= 1

    def stmt(self, n, word='if'):
        k = n.kind
        if k == 'decl':
            vtype, name = n.value
            if name in self.scopes[-1]:
                raise SemanticError(f"Рядок {n.line}: змінна '{name}' вже оголошена")
            if n.children:
                value = self.expr_cast(vtype, n.children[0])
            else:
                value = '0' if vtype == 'int' else '0.0'
            self.scopes[-1][name] = vtype
            self.emit(f'{self.py_name(name)} = {value}')
        elif k == 'assign':
            vtype = self.lookup(n.value, n.line)
            self.emit(f'{self.py_name(n.value)} = {self.expr_cast(vtype, n.children[0])}')
        elif k == 'block':
            self.scopes.append({})
            for st in n.children:
                self.stmt(st)
            self.scopes.pop()
        elif k == 'if':
            self.emit(f'{word} {self.expr(n.children[0])}:')
            self.body(n.children[1])
            if len(n.children) == 3:
                els = n.children[2]
                if els.kind == 'if':
                    self.stmt(els, 'elif')
                else:
                    self.emit('else:')
                    self.body(els)
        elif k == 'while':
            self.emit(f'while {self.expr(n.children[0])}:')
            self.body(n.children[1])
        elif k == 'for':
            # for (init; cond; step) body  ->  init; while cond: body; step
            init, cond, step, body = n.children
            self.stmt(init)
            self.emit(f'while {self.expr(cond)}:')
            self.level += 1
            self.stmt(body)
            self.stmt(step)
            self.level -= 1
        elif k == 'printf':
            args = [self.expr(a) for a in n.children]
            count = n.value.count('%') - 2 * n.value.count('%%')
            if count != len(args):
                raise SemanticError(f'Рядок {n.line}: кількість аргументів printf не відповідає формату')
            if not args:
                text = n.value.replace('%%', '%')
                self.emit(f'print({text!r}, end="")')
                return
            if len(args) == 1:
                tup = f'({args[0]},)'
            else:
                tup = '(' + ', '.join(args) + ')'
            self.emit(f'print({n.value!r} % {tup}, end="")')

    def type_of(self, n):
        if n.kind == 'num':
            return 'float' if isinstance(n.value, float) else 'int'
        if n.kind == 'var':
            return self.lookup(n.value, n.line)
        if n.kind == 'unop':
            return self.type_of(n.children[0]) if n.value == '-' else 'int'
        if n.value in ('+', '-', '*', '/', '%'):
            types = (self.type_of(n.children[0]), self.type_of(n.children[1]))
            return 'float' if 'float' in types else 'int'
        return 'int'

    def is_bool(self, n):
        if n.kind == 'binop':
            return n.value in COMPARE or n.value in ('&&', '||')
        return n.kind == 'unop' and n.value == '!'

    def expr_cast(self, vtype, n):
        code = self.expr(n)
        if vtype == 'int' and self.type_of(n) == 'float':
            return f'int({code})'
        return code

    def expr(self, n, top=True):
        if n.kind == 'num':
            return repr(n.value)
        if n.kind == 'var':
            self.lookup(n.value, n.line)
            return self.py_name(n.value)
        if n.kind == 'unop':
            inner = self.expr(n.children[0], False)
            res = f'-{inner}' if n.value == '-' else f'not {inner}'
            return res if top else f'({res})'

        a, b = n.children
        op = n.value
        if op in ('&&', '||'):
            word = 'and' if op == '&&' else 'or'
            res = f'{self.cond(a)} {word} {self.cond(b)}'
        elif op == '/' and self.type_of(n) == 'int':
            return f'int({self.expr(a)} / {self.expr(b)})'
        elif op == '%':
            if self.type_of(n) != 'int':
                raise SemanticError(f'Рядок {n.line}: операція % тільки для int')
            return f'int(math.fmod({self.expr(a)}, {self.expr(b)}))'
        else:
            res = f'{self.expr(a, False)} {op} {self.expr(b, False)}'
        return res if top else f'({res})'

    def cond(self, n):
        # операнд and/or має бути логічним, щоб результат був 0/1 як у C
        if self.is_bool(n):
            return self.expr(n, False)
        return f'bool({self.expr(n)})'
