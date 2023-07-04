#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

#Ex: 
#escreva('Olá, Mundo!')
#Saída:
#~~~~~~~~~
# Olá, Mundo!
#~~~~~~~~~


def escreva(msg):
    size = len(msg) + 4
    print('~'* size)
    print(f'  {msg}')
    print('~'* size)

escreva('Stefany')

