# UTILIZANDO MÓDULOS

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


# co = cateto oposto
# ca = cateto adjacente 

co = float(input('Qual o cateto oposto?'))
ca = float(input('Qual o cateto adjacente?'))

# hipotenusa = raiz quadrada da soma dos quadrados dos catetos

h = (co ** 2 + ca **2) ** (1/2)

print(f'A hipotenusa é {h:.2f}')

