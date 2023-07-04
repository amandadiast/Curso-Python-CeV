# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
#  if c % 2 == 0:           # se o c for divisivel por 2 - também funciona mas deixa o código mais pesado 

for c in range(2, 51, 2):  # de 2 até 51, pulando de 2 em 2 - deixa o código menor e mais leve
    print(c, end=' ')