# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


people = []
data = []
higher = lower = c = c2 = 0
validate = 'Y'


while validate == 'Y':
    people.append(str(input('What is your name, my dear?   >   ')))
    people.append(float(input('What is your weight?')))
    validate = str(input('Do you wanna continue? [Y/N]  >  ')).upper()
    c += 1
    data.append(people[:])
    if c2 == 0:
        higher = lower = people[1]
    else:
        if people[1] > higher:
            higher = people
        if people[1] < lower:
            lower = people
    people.clear()

print(f'O total de pessoas cadastradas é exatamente: {c} pessoas.')
print(f'Os menores pesos são: ')
for p in data:
    if p[1] <= lower:
        print(p[0])
        
print(f'Os maiores pesos são:  ')
for p in data:
    if p[1] >= higher:
        print(p[0])

