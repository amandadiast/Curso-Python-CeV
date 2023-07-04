# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.


while True:
    genero = str(input('Digite seu genero [M/F]     ')).upper()
    if genero not in 'MF':
        genero = str(input('ERRO - Digite seu gênero novamente: [M/F]  '))
    if genero in 'MF':
        print(f'Seu genero é {genero}, obrigada')  
        break
    