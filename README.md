# Синтаксичний аналізатор підмножини мови C

Лабораторна робота з системного програмування.
Виконала: Пуха Софія, ТК-31

Транслятор написаний на Python з використанням бібліотеки PLY (Python Lex-Yacc).
PLY працює так само, як lex/yacc: лексер описується регулярними виразами, а парсер будується
за граматикою як LALR(1)-аналізатор.

## Що робить програма

1. Лексичний аналіз (`c_lexer.py`) - розбиває текст програми на токени.
2. Синтаксичний аналіз (`c_parser.py`) - перевіряє програму за граматикою і будує AST.
3. Семантичний аналіз і генерація коду (`codegen.py`) - перевіряє оголошення змінних і типи,
   транслює програму на Python (результат у папці `output/`).
4. Обчислення (`interpreter.py`) - виконує програму обходом AST.
5. Візуалізація (`viz/index.html`) - малює AST у браузері за допомогою d3.js.

## Підтримувана підмножина C

- типи `int`, `float`
- оголошення змінних з ініціалізацією і без
- присвоєння, `i++`, `i--`
- арифметика `+ - * / %`, унарний мінус
- порівняння `< > <= >= == !=`, логічні `&& || !`
- `if`, `if-else`, `while`, `for`, блоки `{ }`
- `printf` з форматним рядком
- коментарі `//` та `/* */`

## Граматика (скорочено)

```
program   : stmt_list
stmt_list : stmt_list stmt | empty
stmt      : decl | assign ';' | if_stmt | while_stmt | for_stmt | printf_stmt | block
decl      : type ID ';' | type ID '=' expr ';'
type      : INT | FLOAT
assign    : ID '=' expr | ID '++' | ID '--'
block     : '{' stmt_list '}'
if_stmt   : IF '(' expr ')' stmt | IF '(' expr ')' stmt ELSE stmt
while_stmt: WHILE '(' expr ')' stmt
for_stmt  : FOR '(' assign ';' expr ';' assign ')' stmt
printf_stmt : PRINTF '(' STRING args ')' ';'
args      : args ',' expr | empty
expr      : expr op expr | '-' expr | '!' expr | '(' expr ')' | INT_NUM | FLOAT_NUM | ID
```

Неоднозначність виразів розв'язується таблицею `precedence` (пріоритети і асоціативність операторів).
Конфлікт "висячого else" розв'язується через `%prec IFX`, тому `else` належить найближчому `if`.

## Запуск

```
pip3 install ply
python3 main.py examples/factorial.c
python3 main.py examples/factorial.c -t     # додатково вивести токени
python3 output/factorial.py                 # запуск згенерованого коду
open viz/index.html                         # візуалізація AST
```

Після кожного запуску PLY створює файл `parser.out` з усіма станами LALR-автомата
і списком конфліктів (якщо вони є).

## Приклади

| файл | що перевіряє |
|---|---|
| `arithmetic.c` | арифметика, пріоритети, ціле ділення, float |
| `factorial.c` | цикли while і for |
| `primes.c` | вкладені цикли, if / else if / else, && |
| `dangling_else.c` | висячий else |
| `error_syntax.c` | синтаксична помилка (немає `;`) |
| `error_semantic.c` | використання неоголошеної змінної |
