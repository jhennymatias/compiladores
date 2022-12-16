# ATIVIDADE PRÁTICA - reconhecedor de estruturas em C

from ply import *

contexto = 0

def get_contexto():
    return contexto

# Tabela de simbolos
# {ID {valor, tipo, contexto}}
simbolos = {}


# Palavras reservadas <palavra>:<TOKEN>
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'int' : 'INT',
    'float' : 'FLOAT',
    'main': 'MAIN', 
    'char': 'CHAR'
}

# Demais TOKENS
tokens = [
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    'LPAREN', 'RPAREN', 'LT', 'LE', 'GT', 'GE', 'NE',
    'COMMA', 'SEMI', 'INTEGER', 'FLOATN', 'STRING',
    'ID', 'SEMICOLON', 'RBRACES', 'LBRACES'
] + list(reserved.values())

#t_ignore = ' \t\n'
print(tokens)
def t_REM(t):
    r'REM .*'
    return t

# Definição de Identificador com expressão regular r'<expressão>'
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\^'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RBRACES = r'\}'
t_LBRACES = r'\{'
t_SEMICOLON = r'\;'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'!='
t_COMMA = r'\,'
t_SEMI = r';'
t_INTEGER = r'\d+'
t_FLOATN = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*?\"'

def t_error(t):
    print("ERROR: Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    t.lexer.skip(1)
space = ' '
t_ignore  = space+'\t\n '
# Constroi o analisador léxico
lexer = lex.lex()

def p_inicio(p):
    'inicio : INT MAIN LPAREN RPAREN blocoprincipal'
    print('Conteudo reconhecido com sucesso!')

def p_conteudo(p):
    '''conteudo : declaracoes
                | declaracoes conteudo
                | atribuicoes 
                | atribuicoes conteudo
                | if  
                | if conteudo 
                | empty'''

def p_blocoprincipal(p):
    'blocoprincipal : LBRACES conteudo RBRACES'

def p_ids(p):
    '''ids : COMMA ID
            | COMMA ID ids'''
    simbolos[p[2]] = {'valor': None, 'tipo': None, 'contexto':get_contexto()}
def p_empty(p):
     'empty :'
     pass

def get_contexto():
    return contexto

def p_declaracoes(p):
    '''declaracoes : tipo ID SEMICOLON
                    | tipo ID ids SEMICOLON 
                    | tipo ID EQUALS INTEGER SEMICOLON 
                    | tipo ID EQUALS FLOATN SEMICOLON 
                    | empty'''
    
    if p[3]=='=':
        if p[2] in list(simbolos.keys()):
            raise AssertionError("Variavel com o mesmo nome já declarada!")
        else:
            simbolos[p[2]] = {'valor': p[4], 'tipo': p[1], 'contexto':get_contexto()}
    else:    
        simbolos[p[2]] = {'valor': None, 'tipo': p[1], 'contexto':get_contexto()}        

    
def p_atribuicoes(p):
    '''atribuicoes : ID EQUALS INTEGER SEMICOLON
                    | ID EQUALS FLOATN SEMICOLON'''
    
    if p[1] in simbolos:
        ## aqui faltou verificar tipo da atribuição
        print(str(simbolos[p[1]]['tipo']))
    else:
        raise AssertionError("Variavel não declarada!")

def p_condicao(p):
    '''condicao : ID LT INTEGER
                | ID LE INTEGER 
                | ID LT FLOATN
                | ID GT INTEGER 
                | ID GE FLOATN
                | ID GE INTEGER 
                | ID GT FLOATN
                | ID LE FLOATN'''
    if p[1] in simbolos:
        print("variavel declarada!")
    else:
        raise AssertionError("Variavel não declarada!")

def p_bloco(p):
    '''bloco : LBRACES  conteudo_if RBRACES'''

def p_conteudo_if(p):
    '''conteudo_if : atribuicoes conteudo_if
                    | operacao conteudo_if
                    | if
                    | empty
    '''

def p_if(p):
    '''if   : IF LPAREN condicao RPAREN bloco
            | IF LPAREN condicao RPAREN bloco else'''
    global contexto
    contexto = contexto + 1

def p_else(p):
    '''else : ELSE bloco'''

def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | POWER
                | DIVIDE'''

def p_operacao(p):
    '''operacao : ID EQUALS ID operador ID SEMICOLON operacao 
                | ID EQUALS ID operador INTEGER SEMICOLON operacao
                | ID EQUALS ID operador FLOATN SEMICOLON operacao
                | ID EQUALS INTEGER operador INTEGER SEMICOLON operacao
                | ID EQUALS FLOATN operador INTEGER SEMICOLON operacao
                | ID EQUALS INTEGER operador ID SEMICOLON operacao
                | ID EQUALS FLOATN operador ID SEMICOLON operacao
                | empty'''

def p_tipo(p):
    '''tipo : INT
            | FLOAT 
            | CHAR'''
    p[0] = p[1]


import ply.yacc as yacc
yacc.yacc()

import logging
logging.basicConfig(
    level=logging.INFO,
    filename="parselog.txt"
)

# entrada do arquivo
file = open("input.txt",'r')
data = file.read()

# string de teste como entrada do analisador léxico
lexer.input(data)

# Tokenização
for tok in lexer:
     print(tok)

yacc.parse(data, debug=logging.getLogger())

