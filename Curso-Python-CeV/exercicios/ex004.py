# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Escreva algo e vamos ver seu tipo primitivo:   ')
print('Classe:  ', type(a))
print('É um número?', a.isnumeric())
print('É uma letra?', a.isalpha())



print('Vamos saber como é a soma entre dois numeros?')

n1 = int(input('Qual é o primeiro número?  '))
n2 = int(input('Qual é o segundo número?  '))

soma = n1 + n2

print (f'Pois bem... O resultado foi {soma}')

#teste

soma2 = soma + soma

print(soma2)
