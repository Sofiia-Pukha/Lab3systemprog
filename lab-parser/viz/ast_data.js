// файл створюється програмою main.py
const AST_DATA = {
 "name": "program",
 "value": "",
 "line": 1,
 "children": [
  {
   "name": "decl",
   "value": "int n",
   "line": 3,
   "children": []
  },
  {
   "name": "decl",
   "value": "int k",
   "line": 4,
   "children": []
  },
  {
   "name": "decl",
   "value": "int is_prime",
   "line": 5,
   "children": []
  },
  {
   "name": "for",
   "value": "",
   "line": 7,
   "children": [
    {
     "name": "assign",
     "value": "n",
     "line": 7,
     "children": [
      {
       "name": "num",
       "value": "2",
       "line": 7,
       "children": []
      }
     ]
    },
    {
     "name": "binop",
     "value": "<=",
     "line": 7,
     "children": [
      {
       "name": "var",
       "value": "n",
       "line": 7,
       "children": []
      },
      {
       "name": "num",
       "value": "30",
       "line": 7,
       "children": []
      }
     ]
    },
    {
     "name": "assign",
     "value": "n",
     "line": 7,
     "children": [
      {
       "name": "binop",
       "value": "+",
       "line": 7,
       "children": [
        {
         "name": "var",
         "value": "n",
         "line": 7,
         "children": []
        },
        {
         "name": "num",
         "value": "1",
         "line": 7,
         "children": []
        }
       ]
      }
     ]
    },
    {
     "name": "block",
     "value": "",
     "line": 7,
     "children": [
      {
       "name": "assign",
       "value": "is_prime",
       "line": 8,
       "children": [
        {
         "name": "num",
         "value": "1",
         "line": 8,
         "children": []
        }
       ]
      },
      {
       "name": "assign",
       "value": "k",
       "line": 9,
       "children": [
        {
         "name": "num",
         "value": "2",
         "line": 9,
         "children": []
        }
       ]
      },
      {
       "name": "while",
       "value": "",
       "line": 10,
       "children": [
        {
         "name": "binop",
         "value": "&&",
         "line": 10,
         "children": [
          {
           "name": "binop",
           "value": "<=",
           "line": 10,
           "children": [
            {
             "name": "binop",
             "value": "*",
             "line": 10,
             "children": [
              {
               "name": "var",
               "value": "k",
               "line": 10,
               "children": []
              },
              {
               "name": "var",
               "value": "k",
               "line": 10,
               "children": []
              }
             ]
            },
            {
             "name": "var",
             "value": "n",
             "line": 10,
             "children": []
            }
           ]
          },
          {
           "name": "var",
           "value": "is_prime",
           "line": 10,
           "children": []
          }
         ]
        },
        {
         "name": "block",
         "value": "",
         "line": 10,
         "children": [
          {
           "name": "if",
           "value": "",
           "line": 11,
           "children": [
            {
             "name": "binop",
             "value": "==",
             "line": 11,
             "children": [
              {
               "name": "binop",
               "value": "%",
               "line": 11,
               "children": [
                {
                 "name": "var",
                 "value": "n",
                 "line": 11,
                 "children": []
                },
                {
                 "name": "var",
                 "value": "k",
                 "line": 11,
                 "children": []
                }
               ]
              },
              {
               "name": "num",
               "value": "0",
               "line": 11,
               "children": []
              }
             ]
            },
            {
             "name": "assign",
             "value": "is_prime",
             "line": 12,
             "children": [
              {
               "name": "num",
               "value": "0",
               "line": 12,
               "children": []
              }
             ]
            }
           ]
          },
          {
           "name": "assign",
           "value": "k",
           "line": 13,
           "children": [
            {
             "name": "binop",
             "value": "+",
             "line": 13,
             "children": [
              {
               "name": "var",
               "value": "k",
               "line": 13,
               "children": []
              },
              {
               "name": "num",
               "value": "1",
               "line": 13,
               "children": []
              }
             ]
            }
           ]
          }
         ]
        }
       ]
      },
      {
       "name": "if",
       "value": "",
       "line": 15,
       "children": [
        {
         "name": "var",
         "value": "is_prime",
         "line": 15,
         "children": []
        },
        {
         "name": "printf",
         "value": "\"%d \"",
         "line": 16,
         "children": [
          {
           "name": "var",
           "value": "n",
           "line": 16,
           "children": []
          }
         ]
        }
       ]
      }
     ]
    }
   ]
  },
  {
   "name": "printf",
   "value": "\"\\n\"",
   "line": 18,
   "children": []
  },
  {
   "name": "decl",
   "value": "int x",
   "line": 20,
   "children": [
    {
     "name": "num",
     "value": "15",
     "line": 20,
     "children": []
    }
   ]
  },
  {
   "name": "if",
   "value": "",
   "line": 21,
   "children": [
    {
     "name": "binop",
     "value": "&&",
     "line": 21,
     "children": [
      {
       "name": "binop",
       "value": ">",
       "line": 21,
       "children": [
        {
         "name": "var",
         "value": "x",
         "line": 21,
         "children": []
        },
        {
         "name": "num",
         "value": "10",
         "line": 21,
         "children": []
        }
       ]
      },
      {
       "name": "binop",
       "value": "==",
       "line": 21,
       "children": [
        {
         "name": "binop",
         "value": "%",
         "line": 21,
         "children": [
          {
           "name": "var",
           "value": "x",
           "line": 21,
           "children": []
          },
          {
           "name": "num",
           "value": "2",
           "line": 21,
           "children": []
          }
         ]
        },
        {
         "name": "num",
         "value": "1",
         "line": 21,
         "children": []
        }
       ]
      }
     ]
    },
    {
     "name": "printf",
     "value": "\"%d більше 10 і непарне\\n\"",
     "line": 22,
     "children": [
      {
       "name": "var",
       "value": "x",
       "line": 22,
       "children": []
      }
     ]
    },
    {
     "name": "if",
     "value": "",
     "line": 23,
     "children": [
      {
       "name": "binop",
       "value": ">",
       "line": 23,
       "children": [
        {
         "name": "var",
         "value": "x",
         "line": 23,
         "children": []
        },
        {
         "name": "num",
         "value": "10",
         "line": 23,
         "children": []
        }
       ]
      },
      {
       "name": "printf",
       "value": "\"%d більше 10 і парне\\n\"",
       "line": 24,
       "children": [
        {
         "name": "var",
         "value": "x",
         "line": 24,
         "children": []
        }
       ]
      },
      {
       "name": "printf",
       "value": "\"%d не більше 10\\n\"",
       "line": 26,
       "children": [
        {
         "name": "var",
         "value": "x",
         "line": 26,
         "children": []
        }
       ]
      }
     ]
    }
   ]
  }
 ]
};
const SOURCE_NAME = "primes.c";
const SOURCE_CODE = "/* Прості числа до 30\n   та перевірка числа через if / else if / else */\nint n;\nint k;\nint is_prime;\n\nfor (n = 2; n <= 30; n++) {\n    is_prime = 1;\n    k = 2;\n    while (k * k <= n && is_prime) {\n        if (n % k == 0)\n            is_prime = 0;\n        k++;\n    }\n    if (is_prime)\n        printf(\"%d \", n);\n}\nprintf(\"\\n\");\n\nint x = 15;\nif (x > 10 && x % 2 == 1)\n    printf(\"%d більше 10 і непарне\\n\", x);\nelse if (x > 10)\n    printf(\"%d більше 10 і парне\\n\", x);\nelse\n    printf(\"%d не більше 10\\n\", x);\n";
