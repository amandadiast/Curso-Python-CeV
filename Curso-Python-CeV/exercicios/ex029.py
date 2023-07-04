# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


#O print da multa tem que ficar dentro da identação no ''if''

carro = float(input('Qual a velocidade do carro? '))

if carro > 80:
     
     print('Você está acima da velocidade e foi multado.')

     multa = (carro - 80) * 7

     print(f'Sua multa ficou no valor de: R$ {multa}')

print('Tenha um bom dia! Dirija com segurança')