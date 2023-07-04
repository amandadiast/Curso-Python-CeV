#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):
    i = 0
    print("Analisando os valores recebidos...")
    print('-' *20)
    sleep(2)
    for c in num:
        i += 1
    print(f'Foram infomados {i} valores.')
    print('-' *20)
    if len(num) == 0:
        print(f'O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(num)}.')


maior(2, 9, 13, 16, 4, 5)




