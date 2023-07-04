# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
itens = ('0', 'PEDRA', 'PAPEL', 'TESOURA')
computador = randint(1, 3)
print('BORA JOGAR PEDRA, PAPEL, TESOURA????')
jogador = int(input('SELECIONE UMA OPÇÃO:  [1] PEDRA - [2] PAPEL - [3] TESOURA'))
print(f'Computador jogou: {itens[computador]} e Jogador jogou: {itens[jogador]}')


if computador == 1:   # COMPUTADOR JOGA PEDRA
    if jogador == 1:   #CONTRA PEDRA
        print('EMPATE!')
    elif jogador == 2:   # CONTRA PAPEL
        print('JOGADOR GANHOU')
    elif jogador == 3:   # CONTRA TESOURA
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:  # COMPUTADOR JOGA PAPEL
    if jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE!')
    elif jogador == 3:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVALIDA')
elif computador == 3:   # COMPUTADOR JOGA TESOURA
    if jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    elif jogador == 3:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA')



