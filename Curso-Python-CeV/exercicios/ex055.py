# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for c in range (1, 6):
    peso = float(input(f'Peso número {c}:  '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior} e o menor peso foi {menor}')


# OUTRO JEITO QUE ACHEI MAIS FACIL 

lista=[]  
for count in range(1, 6):
    peso1=float(input(f'Peso da {count}ª pessoa:'))
    lista+=[peso1]   #adiciona os valores de peso na lista
print('')
print('O Maior peso foi:', max(lista))  
print('O Menor peso foi:', min(lista))  
