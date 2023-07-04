# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

maior = 0
menor = 0
variavel = 0

for count in range (1, 4):
    n = int(input('Digite um número:   >   '))
    variavel += 1
    if variavel == 1:
        maior = n
        menor = n 
    if n > maior:
        maior = n 
    if n < menor:
        menor = n

print(f'O maior número é {maior} e o menor é {menor}')
    