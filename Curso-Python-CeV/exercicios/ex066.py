# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

c = 0
soma = 0

while True:
    n = int(input('Digite um número:   '))
    c = c + 1
    soma = soma + n      #soma recebe ele mesmo (que é 0) mais um numero (que sao todos os numeros que a pessoa digitou)
    if n == 999:
        break 

print(f'Foram digitados{c - 1} números e a soma entre eles foi exatamente {soma - 999}')   

# Deixei anotado da forma ''errada'' para mostar como solucionei, segue jeito correto de desconsiderar a flag na contagem:
# while True:
#    n = int(input('Digite um número:   '))
#    if n == 999:
#        break       
#    c = c + 1
#    soma = soma + n