# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint

q = 0

print('-#-' *20)
print('PAR OU IMPAR -  GAME')
while True:
    jogador = int(input('Digite um número    '))
    escolha = str(input('PAR OU IMPAR? [P / I]   ')).upper()
    c = randint(0, 101)
    total = jogador + c
    print(f'Jogador jogou {jogador} e computador jogou {c}, e o total foi {total}')
    while escolha not in 'PI':
        escolha = str(input('PAR OU IMPAR? [P / I]   ')).upper()
    if escolha == 'P':
        if total % 2:
            print('GANHOU')
            q += 1
        else:
            print('PERDEU')
            break
    elif escolha == 'I':
        if total % 1:
            print('GANHOU')
            q += 1
        else:
            print('PERDEU')
            break
print(f'Você fez {q} pontos ')

    
