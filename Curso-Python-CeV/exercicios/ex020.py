# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
alunos = ['Luiza', 'Leticia', 'Flora', 'José']
print(f'Os alunos são: {alunos}')
random.shuffle(alunos)
print(f'A ordem vai ser: {alunos}')



