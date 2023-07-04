# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

allofthem = dict()
golstotal = list()
validate = 'Y'
everyone = []

while validate == 'Y':
    allofthem['nameplayer'] = input('Qual o nome do jogador?    ')
    allofthem['np'] = int(input(f'Quantas partidas o jogador {allofthem["nameplayer"]} jogou?'))
    for c in range(0, allofthem['np']):
        golstotal.append(int(input(f'Quantos gols na partida {c+1}? ')))
    allofthem['gols'] = golstotal[:]
    allofthem['totgols'] = sum(golstotal)
    golstotal.clear()
    validate = str(input('Like to continue?    [Y/N]:   ')).upper()
    everyone.append(allofthem.copy())

#print(everyone)

#for c, allofthem in enumerate(everyone):  #pra cada item, dicionario inteiro enumerado pela lista
 #   print(f'  {c:<4} {allofthem["nameplayer"]:<13} {allofthem["totgols"]:<7} {allofthem["gols"]}')

print('Os jogadores estão separados por numero')
for c, allofthem in enumerate(everyone):
        print(f'  {c:<4} =  {allofthem["nameplayer"]:<13}')
while True:
    choice = int(input('Escolha qual jogador você gostaria de ver as informações:  (666 para sair)'))
    if choice == 666:
        print("Obrigada, tive muita dificuldade em terminar esse desafio mas estou melhorando, por favor me apoie com boas energias")
        break
    print(f'Você escolheu o jogador {(everyone[choice])["nameplayer"]}')
    for c, v in enumerate(everyone[choice]['gols']):
            print(f'   Na partida {c+1} fez {v} gols')
    print(f'Totalizando {everyone[choice]["totgols"]} gols do jogador(a) {(everyone[choice])["nameplayer"]}.')
    




