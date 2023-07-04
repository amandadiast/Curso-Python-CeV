# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Digite um número:    > '))
n2 = int(input('Digite outro número:    > '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
elif n1 == n2:
     print(f'{n1} e {n2} são iguais.')



# FUNÇÃO QUE CALCULA A AREA
# a = b . a 

def mtm ():
    ns1 = int(input('Digite um número para somar:  '))
    ns2 = int(input('Digite outro para somar ao primeiro: '))
    s = ns1 + ns2
    print(f'{ns1} + {ns2} = {s}') 
    nm1 = int(input('Digite um número para multiplicar:  '))
    nm2 = int(input('Digite o segundo número da multiplicação:  '))
    m = nm1 * nm2
    print(f'{nm1} multiplicado por {nm2} é igual a: {m}')
    nd1 = int(input('Digite um número para dividir:  '))
    nd2 = int(input('Digite outro número para dividir pelo primeiro: '))
    d = nd1 / nd2
    print(f'{nd1} dividido por {nd2} é igual a {d:.2f}')


mtm()


