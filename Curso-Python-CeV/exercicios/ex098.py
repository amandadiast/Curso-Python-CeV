#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:

#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

def contador(inicio, fim, passo):
    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c}')
            c += passo
    else:
        if inicio > fim:
            c = inicio
            while c >= fim:
                print(f'{c}')
                c -= passo
    
    
contador(0, 10, 2)
