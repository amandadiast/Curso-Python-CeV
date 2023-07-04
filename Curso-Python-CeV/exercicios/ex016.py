
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# UTILIZANDO MÓDULOS

import math 

n1 = float(input('Digite um número qualquer:  '))

print(f'O valor digitado foi {n1} e a porção inteira de {n1} é {math.trunc(n1)}')


