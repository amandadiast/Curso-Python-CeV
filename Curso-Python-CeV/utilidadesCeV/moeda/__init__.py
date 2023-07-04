def aumentar(preco, taxa, format=False):
    r = preco + (preco * taxa/100)
    return r if format is False else moeda(r)

def diminuir(preco, taxa, format=False):
    r = preco - (preco * taxa / 100)
    return r if format is False else moeda(r)

def dobro(preco, format=False):
    r = preco * 2
    return r if format is False else moeda(r)

def metade(preco, format=False):
    r = preco / 2
    return r if format is False else moeda(r)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def linha():
    print('*.*' *10)

def resumo(preco, taxa):
    linha()
    print('RESUMO DO VALOR'.center(30))
    linha()
    print(f'Aumento: {aumentar(preco,taxa, format=True)}'.center(30))
    print(f'Subtração: {diminuir(preco, taxa, format=True)}'.center(30))
    print(f'Dobro: {dobro(preco, format=True)}'.center(29))
    print(f'Metade: {metade(preco, format=True)}'.center(29))
