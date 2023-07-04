# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

# Resolução: Passar o calculo do t3 para frente, fazer sempre o t1 ser o antepenultimo e o t2 ser o penultimo
# ex:  termo1   termo2   termo 3
#        0    +    1   +    1
# A resolução:
# ex:           termo1   termo2   termo 3
#        0    +    1   +    1  +     ?
# E assim por diante, para nao ter que gerar infinitas variaveis


print('SEQUENCIA DE FIBONACCI 1.0')

termos = int(input('Quantos termos você quer mostrar?   >   '))

termo1 = 0
termo2 = 1

print(f'{termo1} - {termo2} -', end=' ')
cont = 3 #Como ja tenho o primeiro e segundo termo, o contador começa no terceiro

while cont <= termos:
        t3 = termo1 + termo2
        print(f'{t3} - ', end=' ')
        termo1 = termo2   #Acompanhando a resolução, o t1 passa a ser o t2 (anda pra frente)
        termo2 = t3   #O t2 passa a ser o termo3 para gerar o calculo do antepenultimo mais o penultimo
        cont +=1
