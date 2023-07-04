# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo



n = int(input('Digite um número para descobrir se é primo:   '))
total = 0

for count in range(1, n + 1):
    if n % count == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'.{count}', end=' ')
print(f'\n\033[m O número {n} foi dividido por {total} números')

