# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada


n = int(input('Digite um número para descobrir sua tabuada: '))

for c in range(1,11):
    print(f'{c} x {n} = {c * n}')


