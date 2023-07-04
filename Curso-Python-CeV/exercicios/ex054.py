# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Em qual ano você nasceu?  > '))
    if 2023 - nasc >= 18:
        maior +=1
        print('É de maior')
    else:
        menor += 1
        print('É de menor')
print(f'São {maior} de maior e {menor} de menor.')