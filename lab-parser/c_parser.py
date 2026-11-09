# Синтаксичний аналізатор (PLY yacc, LALR(1)) з побудовою AST
import ply.yacc as yacc

from c_lexer import tokens, lexer
from ast_nodes import Node


class ParseError(Exception):
    pass


# пріоритети: чим нижче в списку, тим вищий пріоритет
precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('left', 'LT', 'GT', 'LE', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'UMINUS', 'NOT'),
)


def p_program(p):
    'program : stmt_list'
    p[0] = Node('program', p[1], line=1)


def p_stmt_list(p):
    '''stmt_list : stmt_list stmt
                 | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []


def p_empty(p):
    'empty :'
    pass


def p_stmt(p):
    '''stmt : decl
            | assign SEMI
            | if_stmt
            | while_stmt
            | for_stmt
            | printf_stmt
            | block'''
    p[0] = p[1]


def p_decl(p):
    '''decl : type ID SEMI
            | type ID ASSIGN expr SEMI'''
    children = [p[4]] if len(p) == 6 else []
    p[0] = Node('decl', children, (p[1], p[2]), p.lineno(2))


def p_type(p):
    '''type : INT
            | FLOAT'''
    p[0] = p[1]


def p_assign(p):
    'assign : ID ASSIGN expr'
    p[0] = Node('assign', [p[3]], p[1], p.lineno(1))


def p_assign_inc(p):
    '''assign : ID INC
              | ID DEC'''
    # i++ перетворюється на i = i + 1
    line = p.lineno(1)
    op = '+' if p[2] == '++' else '-'
    expr = Node('binop', [Node('var', value=p[1], line=line), Node('num', value=1, line=line)], op, line)
    p[0] = Node('assign', [expr], p[1], line)


def p_block(p):
    'block : LBRACE stmt_list RBRACE'
    p[0] = Node('block', p[2], line=p.lineno(1))


def p_if(p):
    'if_stmt : IF LPAREN expr RPAREN stmt %prec IFX'
    p[0] = Node('if', [p[3], p[5]], line=p.lineno(1))


def p_if_else(p):
    'if_stmt : IF LPAREN expr RPAREN stmt ELSE stmt'
    p[0] = Node('if', [p[3], p[5], p[7]], line=p.lineno(1))


def p_while(p):
    'while_stmt : WHILE LPAREN expr RPAREN stmt'
    p[0] = Node('while', [p[3], p[5]], line=p.lineno(1))


def p_for(p):
    'for_stmt : FOR LPAREN assign SEMI expr SEMI assign RPAREN stmt'
    p[0] = Node('for', [p[3], p[5], p[7], p[9]], line=p.lineno(1))


def p_printf(p):
    'printf_stmt : PRINTF LPAREN STRING args RPAREN SEMI'
    p[0] = Node('printf', p[4], p[3], p.lineno(1))


def p_args(p):
    '''args : args COMMA expr
            | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = []


def p_expr_binop(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr MOD expr
            | expr LT expr
            | expr GT expr
            | expr LE expr
            | expr GE expr
            | expr EQ expr
            | expr NE expr
            | expr AND expr
            | expr OR expr'''
    p[0] = Node('binop', [p[1], p[3]], p[2], p.lineno(2))


def p_expr_uminus(p):
    'expr : MINUS expr %prec UMINUS'
    p[0] = Node('unop', [p[2]], '-', p.lineno(1))


def p_expr_not(p):
    'expr : NOT expr'
    p[0] = Node('unop', [p[2]], '!', p.lineno(1))


def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]


def p_expr_num(p):
    '''expr : INT_NUM
            | FLOAT_NUM'''
    p[0] = Node('num', value=p[1], line=p.lineno(1))


def p_expr_var(p):
    'expr : ID'
    p[0] = Node('var', value=p[1], line=p.lineno(1))


def p_error(p):
    if p is None:
        raise ParseError('Синтаксична помилка: неочікуваний кінець файлу')
    raise ParseError(f"Синтаксична помилка в рядку {p.lineno}: неочікуваний токен '{p.value}' ({p.type})")


# debug=True - PLY записує таблиці LALR та конфлікти у файл parser.out
parser = yacc.yacc(debug=True, write_tables=False)


def parse(text):
    lexer.lineno = 1
    return parser.parse(text, lexer=lexer)
