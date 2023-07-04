# # Crie um programa que leia um nome que começa ou não com "AMANDA".


n = str(input('Qual o nome e sobrenome?')).strip()

print(n[:6] == 'Amanda')

