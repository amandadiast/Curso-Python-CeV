# OPERADORES ARITMÉTICOS


# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um numero inteiro:    '))
s = num + 1 
a = num - 1

print(f'O sucessor de {num} é o numero {s} e o antecessor de {num} é o numero {a}.')


n1 = int(input('Digite um valor e vamos dissecar ele para aprender: '))


print(f'A soma de {n1} com {n1} é {n1 + n1}')

n2 = float(input('Digite um terceiro valor'))
n3 = float(input('Digite um quarto valor'))

dvs = (n2 / n3)
p2 = n2 ** n2
p3 = n3 ** n3


print(
    f'A divisão entre o terceiro valor e quarto é {dvs:.2f}, a potencia de {n2} é {p2} e a potencia de {n3} é {p3}')

