# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()


aluno['nome'] = str(input('Qual é o nome do aluno?   '))
aluno['media'] = float(input(f'Qual é a média do(a) aluno {aluno["nome"]}?     '))

if aluno['media'] >= 6:
    aluno['status'] = 'BOA'
else:
    if aluno['media']  < 6:
        aluno['status'] = 'RUIM'

for a, b in aluno.items():     # a = keys e b = values
    print(f'\033[0;30;41m{a} \033[m = \033[0;30;41m {b} \033[m \n', end='')