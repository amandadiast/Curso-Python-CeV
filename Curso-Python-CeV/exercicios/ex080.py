#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

import bisect

lst = []

for count in range(5):
    n = int(input('Type a number: '))
    bisect.insort(lst, n)
    print(f'Number {n} included in position {lst.index(n) + 1}')    #index procura a posição do valor

print(lst)