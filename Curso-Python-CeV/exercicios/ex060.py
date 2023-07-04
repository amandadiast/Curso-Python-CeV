# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

n = int(input('Digite um número e vamos ver o seu fatorial: '))
c = n
f = 1 

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c    # ou f *= c
    c-=1         # c recebe ele mesmo - 1 
print(f'{f}')


# OUTRO JEITO =)

n2 = int(input('Digite um número e vamos ver o seu fatorial: '))

f = factorial(n2)

print(f'{n2}! = {f}')
