# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


from random import randint

lst = []


def sorteia(qnt):
    if qnt == 0:
        a = randint(0, 100)
        b = randint(0, 100)
        c = randint(0, 100)
        d = randint(0, 100)
        e = randint(0, 100)
        print(
            f' Primeiro nº sorteado: {a} \n Segundo nº sorteado: {b} \n Terceiro nº sorteado: {c}  \n Quarto nº sorteado: {d}  \n Quinto nº sorteado: {e}')
        lst.append(a)
        lst.append(b)
        lst.append(c)
        lst.append(d)
        lst.append(e)


sorteia(0)


def somaPar(list):
    s = 0  # python so aceitou a declaração de valor dentro da funcao
    print(' Números pares:', end='  ')
    for n in list:
        if n % 2 == 0:
            print(f'{n}', end=' ')


somaPar(lst)
