# expr = str(input('Digite a expressão: '))
# pi = expr.count('(')
# pf = expr.count(')')
# if expr.index(')') > expr.index('('):
#     if pi == pf:
#         print('Expressão válida')
#     else:
#         print('Expressão é inválida')
# else:
#     print('Expressão inválida')

expr = str(input('digite sua expressão '))
pilha = []
for simb in expr: # corre toda a string expr
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('expressão está certa')
else:
    print('expressão está errada')