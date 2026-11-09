# Інтерпретатор: обчислення програми обходом AST
import math


class SemanticError(Exception):
    pass


class Interpreter:
    def __init__(self):
        # стек областей видимості: ім'я -> [тип, значення]
        self.scopes = [{}]

    def run(self, tree):
        for st in tree.children:
            self.exec(st)

    def lookup(self, name, line):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise SemanticError(f"Рядок {line}: змінна '{name}' не оголошена")

    def convert(self, vtype, value):
        return int(value) if vtype == 'int' else float(value)

    def exec(self, n):
        k = n.kind
        if k == 'decl':
            vtype, name = n.value
            if name in self.scopes[-1]:
                raise SemanticError(f"Рядок {n.line}: змінна '{name}' вже оголошена")
            value = self.eval(n.children[0]) if n.children else 0
            self.scopes[-1][name] = [vtype, self.convert(vtype, value)]
        elif k == 'assign':
            var = self.lookup(n.value, n.line)
            var[1] = self.convert(var[0], self.eval(n.children[0]))
        elif k == 'block':
            self.scopes.append({})
            for st in n.children:
                self.exec(st)
            self.scopes.pop()
        elif k == 'if':
            if self.eval(n.children[0]):
                self.exec(n.children[1])
            elif len(n.children) == 3:
                self.exec(n.children[2])
        elif k == 'while':
            while self.eval(n.children[0]):
                self.exec(n.children[1])
        elif k == 'for':
            init, cond, step, body = n.children
            self.exec(init)
            while self.eval(cond):
                self.exec(body)
                self.exec(step)
        elif k == 'printf':
            args = tuple(self.eval(a) for a in n.children)
            try:
                text = n.value % args
            except (TypeError, ValueError):
                raise SemanticError(f'Рядок {n.line}: аргументи printf не відповідають формату')
            print(text, end='')

    def eval(self, n):
        if n.kind == 'num':
            return n.value
        if n.kind == 'var':
            return self.lookup(n.value, n.line)[1]
        if n.kind == 'unop':
            v = self.eval(n.children[0])
            return -v if n.value == '-' else int(not v)

        op = n.value
        # && та || обчислюються скорочено, як у C
        if op == '&&':
            return int(bool(self.eval(n.children[0])) and bool(self.eval(n.children[1])))
        if op == '||':
            return int(bool(self.eval(n.children[0])) or bool(self.eval(n.children[1])))

        a = self.eval(n.children[0])
        b = self.eval(n.children[1])
        both_int = isinstance(a, int) and isinstance(b, int)

        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op in ('/', '%') and b == 0:
            raise SemanticError(f'Рядок {n.line}: ділення на нуль')
        if op == '/':
            # ціле ділення в C відкидає дробову частину
            return int(a / b) if both_int else a / b
        if op == '%':
            if not both_int:
                raise SemanticError(f'Рядок {n.line}: операція % тільки для int')
            return int(math.fmod(a, b))
        if op == '<':
            return int(a < b)
        if op == '>':
            return int(a > b)
        if op == '<=':
            return int(a <= b)
        if op == '>=':
            return int(a >= b)
        if op == '==':
            return int(a == b)
        if op == '!=':
            return int(a != b)
        raise SemanticError(f'Рядок {n.line}: невідомий оператор {op}')
