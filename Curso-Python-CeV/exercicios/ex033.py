# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 =int(input('digite o primeiro número:  '))
n2 =int(input('Digite o segundo número: '))
n3 =int(input ('Digite o terceiro número: '))

l =[n1,n2,n3]

print(f'O menor número é {min(l)}')
print(f'O maior número é {max(l)}')


