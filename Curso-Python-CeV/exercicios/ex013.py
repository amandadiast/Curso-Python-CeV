#AUMENTO DE SALARIO

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual o seu salário?'))

aumento = s + (s * 15 / 100)

print(f'O salário, que era R${s}, com o aumento de 15%, ficou R${aumento}')