#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from utilidadesCeV import moeda

m = float(input('Digite o preço:  R$'))
t = float(input('Digite a taxa:   '))


ask = int(input('O QUE VOCÊ QUER FAZER AGORA?  1 - AUMENTAR 2 - DIMINUIR  3 - DOBRAR  4 - METADE  '))

if ask == 1:
    print(moeda.aumentar(m, t, format=True))
if ask == 2:
    print((moeda.diminuir(m, t, format=True)))
if ask == 3:
    print(moeda.dobro(m, format=True))
if ask == 4:
    print(moeda.metade(m, format=True))