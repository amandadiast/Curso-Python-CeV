# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


from random import randint
a = 0
c2 = []  #composite
ngames = int(input('How many times you wanna play?    > '))
print('-' *20)
for c in range(0, ngames):
    while len(c2) < 6:
        n = randint(1, 60)
        if a == 0:
            c2.append(n)
    print(f'Jogo {c + 1} : {sorted(c2)}')
    c2.clear()

