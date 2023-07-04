#  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


nlst = []
valid = 'S'
c = 0
five = 0

while valid == 'S':
   n = int(input('Digite um número: '))
   valid = str(input('Quer continuar?  [S/N]   ')).upper()
   nlst.append(n)
   c += 1
   if n == 5:
    five += 1

nlst.sort()
nlst.reverse()

print(f'Foi digitado {c} números')
print(f'Lista de valores em ordem decrescente: {nlst}')

if five == 0:
    print('O número 5 não apareceu!')
    
if five >= 1:
    print(f'O número 5 apareceu e foi contado {five} vezes')

