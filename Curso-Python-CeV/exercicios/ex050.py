# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for c in range (1, 7):
    n = int(input('Digite um número:  '))
    if n % 2 == 0:
        soma = soma + n   #ou soma += n
        cont = cont + 1   #ou cont += 1
print(f' foram {cont} números pares e a soma deles é: {soma}')
