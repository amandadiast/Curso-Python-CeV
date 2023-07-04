# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

values = []
valid = 'S'

while valid == 'S':
    n = int(input('Digite um valor:   '))
    valid = str(input('Quer continuar?  [S/N]   ')).upper()
    values.append(n)

print(f'LISTA GERAL: {values}')

print('Lista com apenas números pares:   ')
par = list (n2 for n2 in values if n2 % 2 == 0)
print(par)

print('Lista com apenas números ímpares:   ')
impar = list (n2 for n2 in values if n2 % 2 == 1)
print(impar)