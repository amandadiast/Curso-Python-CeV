#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

lst = []
mulheres = []
soma = 0
validacao = 'S'
print("*DADOS*")

while True:
    nome = (input("Nome:         "))
    sexo = (input("Sexo [M/F]:         ")).upper()
    idade = int(input("Idade:        "))  
    p = dict()
    p['nome'] = nome
    p['sexo'] = sexo
    p['idade'] = idade
    if sexo == 'F':
        mulheres.append(nome)
    lst.append(p.copy())
    if validacao == 'S':
        validacao = (input('Quer continuar cadastrando mais pessoas?   [S/N]')).upper()
    if validacao == 'N':
        break

for c in range(0, len(lst)):
    soma += lst[c]['idade']
    
media = soma / 2

print(lst)
print(f'Foram cadastradas {len(lst)} pessoas.')
print(f'A soma das idades foi: {soma}')
print(f'A média entre de idades das pessoas cadastradas é de: {media} anos.')
print(f'Foram cadastradas as seguintes mulheres: {mulheres}')

for c in lst:    # para cada item na lista
    if c['idade'] > media:   # de cada item da lista dentro das idades for maior que a média
        print(f'As pessoas com idade acima da média que é {media} anos, são: {c["nome"]}') #cada item da lista dentro de nome q tem cada item da lista dentro de idade maior que a media
        



