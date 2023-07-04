# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

name = str(input('Digite o seu nome: ')).strip()
if name.upper().find('SILVA') > -1:
    print('Você tem Silva no nome!')
else:
    print('Você não tem Silva no nome!')

# o find vai me dar qualquer qualquer valor igual ou maior que zero caso tenha silva no nome. 
# Entao se o find retornar algo maior que -1, ele printa que eu tenho Silva no nome, senao, printa que eu nao tenho.


