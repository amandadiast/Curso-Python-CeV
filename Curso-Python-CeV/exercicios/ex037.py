#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher 
#qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número:  > '))
op = int(input('DIGITE UMA OPÇÃO:     [2] - TRANSFORMAR EM BINÁRIO   [8] - TRANSFORMAR EM OCTAL   [16] - TRANSFORMAR EM HEXADECIMAL             '))

if op == 2:
  print(f'BINÁRIO: {(bin(n)[2:])}')
elif op == 8:
  print(f'OCTAL: {(oct(n)[2:])}')
elif op == 16:
  print(f'HEXADECIMAL: {(hex(n)[2:])}')

