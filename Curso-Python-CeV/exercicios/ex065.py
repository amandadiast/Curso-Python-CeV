# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

#Observação minha: Posso botar um input dentro do while mesmo que ja tenho declarado a variavel antes


validate = 'S'
cont = 0
soma = 0

while validate in 'S':
    n = int(input('Digite um número inteiro: '))
    validate = str(input('Quer continuar?   [S]  - [N]  >    ')).upper()
    cont += 1
    soma = soma + n

media = soma / cont
print(f'A média dos números digitados é exatamente {media:.0f}, obrigado(a) por utilizar nossa calculadora')

