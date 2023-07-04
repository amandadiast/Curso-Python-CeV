# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida


p = float(input('Qual é o seu peso?    >   '))
a = float(input('Qual é a sua altura?   >  '))

imc = p / (a ** 2)

if imc.is_integer() < 18.5:
    print('ABAIXO DO PESO')
elif imc.is_integer() > 18.5 and imc <= 25:     # poderia ser:  elif 18.5 <= imc < 25:    se o imc esta entre 18 e 25...
    print('PESO IDEAL')
elif imc.is_integer() > 25 and imc <= 30:
    print('SOBREPESO')
elif imc.is_integer() > 30 and imc <= 40:
    print('OBESIDADE')
elif imc.is_integer() > 40:
    print('OBESIDADE MÓRBIDA')
