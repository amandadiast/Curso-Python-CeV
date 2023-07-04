#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
from math import factorial

def fatorial(n=0, show=False):
    f = factorial(n)
    if show == True:
        print(f'{n}! = {f}')

fatorial(3, show=True)

#or

def fatorial2way(n,show=False):
    c = n
    f = 1 
    while c > 0:
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')  #bota x se o numero é maior que 1 e quando acaba bota =
        f = f * c    # ou f *= c
        c-=1         # c recebe ele mesmo - 1 
    if show==True:
        print(f'{f}')

fatorial2way(3,show=True)