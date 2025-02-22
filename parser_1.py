import ply.yacc as yacc
from lex import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_program(p):
    '''program : declaration_list'''
    p[0] = ('program', p[1])

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_declaration(p):
    '''declaration : var_declaration
                   | statement'''
    p[0] = p[1]

def p_var_declaration(p):
    '''var_declaration : INT ID'''
    p[0] = ('declare', p[2])

def p_statement(p):
    '''statement : expression_statement'''
    p[0] = p[1]

def p_expression_statement(p):
    '''expression_statement : ID EQUALS expression'''
    p[0] = ('assign', p[1], p[3])

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | NUMBER
                  | ID'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()
