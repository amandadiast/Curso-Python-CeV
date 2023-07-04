# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 

#np = number partidas (ver como é partidas em ingles kkk)
program = dict()
golst = list()
gols = 0
program['nameplayer'] = input('Qual o nome do jogador?    ')
program['np'] = int(input(f'Quantas partidas o jogador {program["nameplayer"]} jogou?'))
for c in range(0, program['np']):
    golst.append(int(input(f'Quantos gols na partida {c+1}? ')))
    gols += golst[c]
program['gols'] = golst
program['totalgols'] = gols

print(program.items())