#  Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

n = str(input('O nome a ser analisado é:  ')).strip()

n2 =  len(n) - n.count(' ')
prinom = n.split() 

print('='*20) 

print(f'Em letras maisculas fica: {n.upper()}')
print(f'Em letras minusculas fica: {n.lower()}')
print(f'O numero total de letras nesse nome é: {n2} letras')
print(f'O primeiro nome é: {prinom [0]}')


# Ache o primeiro e ultimo nome de pessoas com muitos sobrenomes

nome = str(input('Qual o nome completo da pessoa?')).strip()
nomes = nome.split()
print(f'O primeiro nome é {nomes[0]}')
print(f'O ultimo nome é {nomes[len(nomes)-1]}')
