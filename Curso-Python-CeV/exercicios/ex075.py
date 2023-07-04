# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# variavel tem q ser antes do for 


values = tuple(int(input('Digite valores ')) for c in range(1, 5))

print(f'O numero nove apareceu {values.count(9)} vezes')    #count para contar
print(f'P 3 foi digitado pela primeira vez na posição: {values.index(3) + 1}')    #index acha o valor dentro da tupla 
print(f'Os números pares foram: ', end=' ')

for n in values:
    if n % 2 == 0:
        print(n)


