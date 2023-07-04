# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
alunos = ['Luiza', 'Leticia', 'Flora', 'José']

escolha = random.choice(alunos)
print(f'Os alunos são: {alunos}')
print(f'O escolhido(a) foi: {escolha}')





