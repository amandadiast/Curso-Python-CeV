#Conversor de moedas

# Dolar = 4,91

#PARA LIMITAR CASAS DECIMAIS : :.2F (EXEMPLO)

R = float(input('Quanto você tem na conta? R$'))

D = R / 4.91

print(f'Com R${R:.2f} você consegue comprar, em dolar: R${D:.2f}')
