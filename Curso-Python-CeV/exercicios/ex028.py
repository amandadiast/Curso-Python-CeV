# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
from time import sleep

comp = random.randint(0, 6)
print('COMPUTADOR ESTA PENSANDO EM UM NÚMERO...')
sleep(0.5)
print('CARREGANDO....')
sleep(1.0)
jogador = int(input('Qual número o computador pensou? '))

if jogador == comp:
    print('BOA, VOCÊ ACERTOU')
else:
    print('Poxa, não foi dessa vez')


