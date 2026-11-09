# Лексичний аналізатор для підмножини мови C
import ply.lex as lex


class LexError(Exception):
    pass


reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'printf': 'PRINTF',
}

tokens = [
    'ID', 'INT_NUM', 'FLOAT_NUM', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'INC', 'DEC',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',
    'AND', 'OR', 'NOT',
    'ASSIGN',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA',
] + list(reserved.values())

t_INC = r'\+\+'
t_DEC = r'--'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COMMA = r','

t_ignore = ' \t\r'


def t_ignore_COMMENT(t):
    r'//[^\n]*'
    pass


def t_ignore_BLOCK_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_FLOAT_NUM(t):
    r'\d+\.\d*|\.\d+'
    t.value = float(t.value)
    return t


def t_INT_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"([^"\\\n]|\\.)*"'
    s = t.value[1:-1]
    s = s.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"')
    t.value = s
    return t


def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    raise LexError(f"Лексична помилка в рядку {t.lexer.lineno}: невідомий символ '{t.value[0]}'")


lexer = lex.lex()
