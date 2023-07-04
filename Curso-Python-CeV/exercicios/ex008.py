# Conversor de medidas 
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Quantos metros?'))

cm = metros * 100
mm = metros * 1000

print(f'A medida em metros {metros}, é, em cm: {cm}, e em mm: {mm}')
