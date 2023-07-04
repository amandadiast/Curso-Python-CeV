# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 


total1 = 0
totam20 = 0
totalh = 0
while True:
    idade = int(input('Digite a idade dessa pessoa:  '))
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Digite o genêro dessa pessoa:  [M/F]  ')).upper().strip()[0]
    if idade >= 18:
        total1 += 1
    if genero == 'M':
        totalh += 1
    if idade < 20 and genero == 'F':
        totam20 += 1
    v = ' '
    while v not in 'SN':
        v = str(input('Quer continuar?  [S/N]  ')).upper()
    if v == 'N':
        break
print(f'São {total1} pessoas com mais de 18 anos, {totam20} mulheres com menos de 20 anos e {totalh} homens cadastrados')
