#  Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Digite aqui a sua primeira nota:   > '))
n2 = float(input('Digite aqui a sua segunda nota:   >  '))

media = (n1 + n2) / 2

if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('EM RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')

# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

from time import sleep

def msg1(a1, a2, a3):
    print(f'Contagem de {a1} até {a2} em {a3}.')


def para(x, y, z):
    for contador1 in range(x, y, z):
        print(contador1, end=' ')
        sleep(0.4)


def contador(a, b, c):
    if a < b:    #SE O INICIO FOR MENOR QUE O FINAL 
        if c == 0:      #SE A CONTAGEM FOR 0
            msg1(a, b, '1')  
            para(a, b+1, 1)
            print('FIM!')
        else:
            msg1(a, b, c)
            para(a, b + 1, c)
            print('FIM!')
    elif a > b:    #SE O INICIO É MAIOR QUE O FINAL
        if c == 0:
            msg1(a, b, '1')
            para(a, b - 1, -1)
            print('FIM!')
        elif c < 0:
            msg1(a, b, abs(c))
            para(a, b - 1, c)
            print('FIM!')
        else:
            msg1(a, b, abs(c))
            para(a, b - 1, -c)
            print('FIM!')


inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
