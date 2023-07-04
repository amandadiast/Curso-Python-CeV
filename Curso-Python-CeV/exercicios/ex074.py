# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


from random import randint


q = str(input('Quer ver o sorteio?')).upper()
if q == 'SIM':
    aleatorio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
    print(f'Os números sorteados foram: {aleatorio}')
    print(f'O maior é {max(aleatorio)} e o menor é {min(aleatorio)}')
elif q == 'NAO':
     print('Que pena')




#1 -  from random import sample

#a = tuple(sample(range(10), 5))
#print(a)
#print(f'O maior valor é {max(a)} e o menor é {min(a)}.')


# 2 - from random import randint

# numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# print('Os valors sorteados foram: ', end=' ')
# for n in numeros
# print(f'{n}',end=''')