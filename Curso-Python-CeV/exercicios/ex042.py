# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

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
