# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

idade = int(input('Qual é a sua idade?   >  '))

if idade <= 9:
    print('ATLETA MIRIM')
elif idade > 9 and idade <= 14:
    print('ATLETA INFANTIL')
elif idade > 14 and idade <= 19:
    print('ATLETA JÚNIOR')
elif idade > 19 and idade <= 25:
    print('ATLETA SÊNIOR')
elif idade > 25:
    print('ATLETA MASTER')



# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:   

from time import sleep
import emoji

def msg (v1, v2, v3):
    print(emoji.emojize(f'Vamos ver o número {v1} até o {v2} em {v3} passos :red_heart:'))
    


def calculo (vv1, vv2, vv3):
    for calculo1 in range(vv1, vv2, vv3):    #o terceiro numero do range sempre indica de quanto em quanto vai ser a contagem
        print(calculo1, end=' ')
        sleep(0.5)

def contador (i, f, p):
    if i < f:
        if p == 0:
            msg(i, f, p)
            calculo(i, f + 1, 1)
        else:
           msg(i, f, p)
           calculo(i, f + 1, p)
    elif i > f:
         if p == 0:
            msg(i, f, p)
            calculo(i, f - 1, - 1)
         else:
           msg(i, f, p)
           calculo(i, f - 1, - p)


ini = int(input('Inicio:  '))
fi = int(input('Fim:  '))
pa = int(input('Passos:  '))
contador(ini, fi, pa)
