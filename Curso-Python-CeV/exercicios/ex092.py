# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

#Pelas regras atuais, não incluindo as regras de transição, têm direito à aposentadoria os homens que completarem 65 anos
# Enquanto para mulheres a idade mínima é de 61 anos.


p = dict()
p['name'] = str(input('Qual é o nome?   '))
p['gender'] = str(input('Qual o genero? [F/M]    ')).upper()

if p['gender'] == 'F':
    print('Senhorita', end='')
elif p['gender'] == 'M':
        print('Senhor', end='')

p['birthyear'] = float(input(f' {p["name"]}, qual é o seu ano de nascimento?  '))
p['ctps'] = float(input('Qual o número da CTPS: '))


if p['ctps'] != 0:
    p['contyear'] = int(input('Qualé o ano de contratação?  '))
    p['sal'] = float(input('Qual é o salário?    '))

c1 = 2023 - p['birthyear'] 

if p['gender'] == 'F' and c1 >= 61:
    print('Você tem idade o suficiente para se aposentar')
elif p['gender'] == 'F' and c1 < 61:
    print(f'Falta {61 - c1} anos para você se aposentar')


if p['gender'] == 'M'and c1 >= 65:
        print('Você tem idade o suficiente para se aposentar')
elif p['gender'] == 'M'and c1 < 65:
        print(f'Falta {65 - c1} anos para você se aposentar')