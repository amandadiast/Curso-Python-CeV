# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
from time import sleep


validate = 'S'
areas = []


def area(b, a):
    a = base * altura
    print(a)


def title(msg):
    print('*--_--*' * 20)
    print(f"{msg : >65}")
    print('*--_--*' * 20)


def loading(msg):
    print(f"{msg : >65}")


while validate == 'S':
    nome = input(('Nome do usuário:    '))
    base = float(input('Qual é a base?   '))
    altura = float(input('Qual é a altura?    '))
    validate = (input('Quer continuar?    [S/N]')).upper()
    if validate not in 'SN':
        print("Digite apenas 'S' para sim e 'N' para não")
        validate = (input('Quer continuar?    [S/N]')).upper()
    dic = {}
    dic['nome'] = nome
    dic['base'] = base
    dic['altura'] = altura
    areas.append(dic)

print(' NÚMERO IDENTIFICADOR DE CADA USUARIO:')
for c, dic in enumerate(areas):
    print(f'{c:<4} =  {dic["nome"]:<13}')

escolha = int(
    input('Você quer saber o resultado da área de qual usuário?  '))

base = areas[escolha]['base']
altura = areas[escolha]['altura']

title('CALCULADORA')
sleep(2)
loading('CARREGANDO...')
sleep(2)
print(f'Você escolheu o usuário: {areas[escolha]["nome"]}, que possui a base {base} e a altura {altura}, gerando uma area de: ')
area(base,altura)
print('metros quadrados')