# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Não é necessário fazer as três somas para verificar a possibilidade de um triângulo existir.
#  Basta fazer a soma entre os dois lados menores. Se a soma entre eles for maior que o terceiro lado, então, 
# a soma entre qualquer um deles e o terceiro lado (que é o maior) terá o mesmo resultado.

r1 = float(input('Qual é o comprimento da primeira reta?   > '))
r2 = float(input('Qual é o comprimento da segunda reta?   > '))
r3 = float(input('Qual é o comprimento da terceira reta?   > '))

calc1 = r1 + r2
calc2 = r1 + r3
calc3 = r2 + r3

if (r3 < calc1) and (r2 < calc2 ) and (r1 < calc3):
    print('É UM TRIANGULO')
else:
    print('Não é um triangulo')


# JEITO QUE PEGUEI DE OUTRO USUARIO

    print('*' * 54)
print('------- Condição de existência de um triângulo -------'.upper())
print('*' * 54)

r1 = float(input('Informe o comprimento da 1ª reta: '))
r2 = float(input('Informe o comprimento da 2ª reta: '))
r3 = float(input('Informe o comprimento da 3ª reta: '))

sit_1 = ((r2 - r3) < r1 < (r2 + r3))
sit_2 = ((r1 - r3) < r2 < (r1 + r3))
sit_3 = ((r1 - r2) < r3 < (r1 + r2))

if (sit_1 and sit_2 and sit_3):
    print('PARABÉNS! É possível formar um triângulo com essas retas!')
else:
    print('DESCULPA. Não é possível formar um triângulo com essas retas.')

