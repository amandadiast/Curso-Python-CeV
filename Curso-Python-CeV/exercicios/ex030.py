#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = 1 #número ganha 1
par = impar = 0  #Par e impar são iguais a zero (sim da pra fazer dessa forma)
while num != 0:  #Enquanto o número for diferente de 0 (enquanto não for digitado 0)
    num = int(input('Digite um número'))   #Pedindo para digitar um número
    if num  % 2 == 0: #Se o resto da divisão por 2 for igual a 0
        par += 1  #Par recebe par +1
    else:
        impar += 1
print(f'Você digitou {par} números pares e {impar} números impares')


nmr = 1

while nmr != 0:
    nmr = int(input('Em média, de 1 a 10, quantas vezes por dia você tosse?  '))
    if nmr <= 5:
        print('Você é saudavel')
    else:
        print('Você é porca')

print('OVER')


