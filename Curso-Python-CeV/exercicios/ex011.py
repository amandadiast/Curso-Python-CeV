# PINTANDO UMA PAREDE


n = str(input('Qual seu nome?'))


largura = float(input(f'Qual a largura da parede, {n}?  '))
altura = float(input('E a altura?   '))

area = largura * altura


t = area / 2 

print(f'Então {n}, para pintar sua parede, precisaremos de {t}L de tinta.')
