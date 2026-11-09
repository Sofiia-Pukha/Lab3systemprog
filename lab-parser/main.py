# Запуск: python3 main.py <файл.c> [-t]
import json
import os
import sys

from c_lexer import lexer, LexError
from c_parser import parse, ParseError
from interpreter import Interpreter, SemanticError
from codegen import CodeGen

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def print_tokens(source):
    print('=== Токени ===')
    lexer.lineno = 1
    lexer.input(source)
    for tok in lexer:
        print(f'{tok.lineno:3}  {tok.type:10} {tok.value!r}')
    print()


def save_ast(tree, source, filename):
    # дані для візуалізації записуються як js-файл, щоб сторінка працювала без сервера
    path = os.path.join(BASE_DIR, 'viz', 'ast_data.js')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('// файл створюється програмою main.py\n')
        f.write('const AST_DATA = ' + json.dumps(tree.to_dict(), ensure_ascii=False, indent=1) + ';\n')
        f.write('const SOURCE_NAME = ' + json.dumps(filename, ensure_ascii=False) + ';\n')
        f.write('const SOURCE_CODE = ' + json.dumps(source, ensure_ascii=False) + ';\n')


def main():
    if len(sys.argv) < 2:
        print('Використання: python3 main.py <файл.c> [-t]')
        return

    path = sys.argv[1]
    with open(path, encoding='utf-8') as f:
        source = f.read()
    filename = os.path.basename(path)
    name = os.path.splitext(filename)[0]

    try:
        if '-t' in sys.argv:
            print_tokens(source)

        tree = parse(source)
        print('=== AST ===')
        tree.print_tree()
        save_ast(tree, source, filename)
        print('\nAST збережено у viz/ast_data.js, відкрийте viz/index.html')

        code = CodeGen().generate(tree)
        out_dir = os.path.join(BASE_DIR, 'output')
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, name + '.py'), 'w', encoding='utf-8') as f:
            f.write(code)
        print(f'\n=== Згенерований код (output/{name}.py) ===')
        print(code)

        print('=== Результат виконання (інтерпретатор) ===')
        Interpreter().run(tree)
    except (LexError, ParseError, SemanticError) as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
