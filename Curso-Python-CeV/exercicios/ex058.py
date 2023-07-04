ex058.py
# Jogo adivinhação 2

c = randint(0, 5)

j1 = str(input('Vamos jogar??'))

if j1 == 'SIM':

    j2 = int(input('Qual número estou pensando?'))

else:
    print('Nao deu certo não')


if j2 == c:
    print('Boa! ')

else:
    print('Tenta de novo')
