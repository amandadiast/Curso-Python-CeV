# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nc = str(input('Qual o seu nome completo?')).split()
print(f'Primeiro nome = {nc[0]}, Ultimo nome = {nc [len(nc) - 1]}') 

# TREINANDO WHILE COM COMENTARIOS


n = 1 #número ganha 1
while n != 0:  #Enquanto o número for diferente de 0 (enquanto não for digitado 0)
    n = int(input('Digite um número'))   #Pedindo para digitar um número
print('acabou')