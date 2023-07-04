# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from utilidadesCeV import moeda

m = float(input('Digite o preço:  R$'))
t = float(input('Digite a taxa:   '))


ask = int(input('O QUE VOCÊ QUER FAZER AGORA?  1 - AUMENTAR 2 - DIMINUIR  3 - DOBRAR  4 - METADE  '))

if ask == 1:
    print(f'R$ {moeda.aumentar(m, t)}')
if ask == 2:
    print(f'R$ {moeda.diminuir(m, t)}')
if ask == 3:
    print(f'R$ {moeda.dobro(m)}')
if ask == 4:
    print(f'R$ {moeda.metade(m)}')
