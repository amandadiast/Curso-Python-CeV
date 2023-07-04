# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

CRED = '\033[42m'
CEND =  '\033[0m'

CRED1 = '\033[45m'
CEND2 = '\033[0m'

compra = float(input(CRED + 'Qual vai ser o preço da compra?  >  ' + CEND))

condi = int(input(CRED + '''Qual vai ser a condição de pagamento? 
 [1] À vista dinheiro/cheque: 10% de desconto  
 [2] À vista no cartão: 5% de desconto
 [3] Em até 2x no cartão: preço formal  
 [4] 3x ou mais no cartão: 20% de juros >   ''' + CEND  ))

if condi == 1:
    print(CRED1 + f'A compra ficou R${compra - (compra * 10 / 100)}' + CEND2)
elif condi == 2:
   print(CRED1 + f'A compra ficou R$ {compra - (compra * 5 / 100)}' + CEND2)
elif condi == 3:
    print(CRED1 +  f'A compra ficou R$ {compra / 2} por mês' + CEND2)
elif condi == 4:
    print(CRED1 + f'A compra ficou R$ {compra + (compra * 29 / 100)}' + CEND2)

