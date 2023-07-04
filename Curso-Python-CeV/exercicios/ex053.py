# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.


frase = str(input('Digite uma frase:     ')).strip().upper()

if frase[0] == frase[-1]:
    print(f' A FRASE {frase} É UM PALINDROMO')
else:
    print(f'A frase {frase[::-1]} não é palindromo')