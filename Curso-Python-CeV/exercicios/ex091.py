# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
print('\033[0;30;41mJOGO\033[m \033[0;30;41m\033[0;30;41mDE\033[m \033[0;30;41mDADOS\033[m, \033[0;30;41mBORA\033[m \033[0;30;41mLA\033[m \033[0;30;41m!\033[m')
jogadores = {'j1': randint(0, 8), 'j2': randint(0, 8), 'j3': randint(0, 8), 'j4': randint(0, 8)}
jogadoresord = dict()
jogadoresord = sorted(jogadores.items(), key=itemgetter(1), reverse=True)   #o reverse é para botar o jogador vencedor em primeiro, o maior numero em primeiro
for k, v in enumerate(jogadoresord):
    print(f'No dado o {v[0]} tirou o número {v[1]}')
print(f'FICANDO ASSIM:')
for k, v in enumerate(jogadoresord):
    print(f'{k + 1}º LUGAR:  {v[0]}, com {v[1]} ponto(s)! ')
if jogadoresord[0][1] == 8:
    print(f'E o jogador vencedor chamado {jogadoresord[0][0]} ainda tirou 8 no dado.')
else:
    print('FIM')