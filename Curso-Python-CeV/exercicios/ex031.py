# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

n = str(input('Qual é o seu nome? '))
distancia = float(input(f'Qual a distância em KM da sua viagem, {n}?'))

calc1 = 0.50 * distancia
calc2 = 0.45 * distancia


if distancia <= 200:
    print(f'O valor da sua passagem vai ser de:{calc1:.2f}')
else:
    print(f'O valor da sua passagem vai ser de:{calc2:.2f}')
    