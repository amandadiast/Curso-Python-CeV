# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nomejogador='<desconhecido>', gols=0):
      print(f'O jogador {nomejogador}, fez {gols} gols.')


n = str(input('Nome: '))
g = str(input('Quantidade de gols?'))   #esta como string para poder  ficar vazio caso a pessoa nao digitar nada

if g.isnumeric():
    int(g)
else:
    g = 0

if n.strip() == '':   #se sem os espaços ainda estiver vazio
    ficha(gols = g)
else:
    ficha(n, g)   