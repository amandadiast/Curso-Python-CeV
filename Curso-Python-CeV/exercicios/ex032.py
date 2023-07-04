
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# o simbolo de porcentagem (%) serve pra calcular o resto da divisão


ano = int(input('Esse ano é bissexto? Escreva o ano e vamos analisar ou toque 0 e vamos analisar o ano atual'))

# o simbolo de porcentagem (%) serve pra calcular o resto da divisão
#Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando ele com 365 dias,
#um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro
#anos ****(EXCETO ANOS MÚLTIPLOS DE 100 QUE NÃO SÃO MÚLTIPLOS DE 400)****

# O numero tem que ser divisivel por 4 (% 4) e também não pode ser  divisivel por 100, diferente de 0 (!= 0) e divisivel por 400 (% 400):
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano é bissexto')

else:
    print('Não é bissexto')


# A -  Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual é o seu peso?'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido é de:{maior}')
print(f'O menor peso lido é de: {menor}')


# B - Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o 1º número:  '))
n2 = int(input('Digite o 2° número:  '))
n3 = int(input('Digite o 3° número:  '))

if n1<n2 and n1<n3:
    me = n1
if n2<n1 and n2<n3:
    me = n2
if n3<n1 and n3<n2:
    me = n3
if n1>n2 and n1>n3:
    ma = n1
if n2>n1 and n2>n3:
    ma = n2
if n3>n1 and n3>n2:
    ma = n3

print(f'O maior número é {ma} e o menor é {me}')

# C - Faça um programa que leia três números e mostre qual é o maior e qual é o menor - OUTRO JEITO
print('-' *20)
print('SEGUNDO JEITO')
print('-' *20)
n1 = int(input('Digite o 1º número:  '))
n2 = int(input('Digite o 2° número:  '))
n3 = int(input('Digite o 3° número:  '))

ma = n1
if n2>n1 and n2>n3:
    ma = n2
if n3>n1 and n3>n2:
    ma = n3
me = n1
if n2<n1 and n2<n3:
    me = n2
if n3<n1 and n3<n2:
    me = n3

print(f'O maior número é {ma} e o menor é {me}')