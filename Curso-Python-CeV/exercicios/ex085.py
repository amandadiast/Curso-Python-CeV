# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

user = [[], []]
for c in range(1, 8):
    number = int(input('Digite um valor: '))
    if number % 2 == 0:
            user[0].append(number)
    if number % 2 == 1:
            user[1].append(number)

user.sort()

print('Os números pares são, em ordem:')
print(user[0])
print('e os impares são, em ordem:')
print(user[1])

