# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

v = 0
soma = 0 
somamil = 0
maisbarato = ' '
while True:
    np = str(input('Qual é o nome do produto?   >  '))
    p = float(input('Qual é o preço do produto?   >  '))
    v += 1
    soma += p
    if soma > 1000:
        somamil += 1
    if v == 1:
        menor = p
        maisbarato = np
    else:
        if p < menor:
            menor = p
            maisbarato = np
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'A soma dos produtos é de: R${soma:.2f} e a quantidade de produtos que custam mais de mil reais é: {somamil} e o mais barato é o produto {maisbarato}.')
