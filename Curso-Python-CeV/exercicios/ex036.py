# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


casa = float(input('Qual é o valor da casa?      >'))
salario = float(input('Qual é o seu salário     >'))
anos = float(input('Em quantos anos vai pagar?    >'))

pres = casa / (anos * 12)
presmin = salario * 30 / 100

if pres <= presmin:
    print(f'Serão prestações de: R${pres:.2f} por mes.   -  EMPRESTIMO APROVADO  -')

else:
    print('NÃO APROVADO')
