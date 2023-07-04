# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

c1 = 0
exp = str(input('Digite a expressão:     '))

for cada in exp:
    if cada == '(':
        c1 += 1 
    elif cada == ')':
        c1 += -1

if c1 == 0:
    print('Expressão correta')
else:
    print('Expressão incorreta')