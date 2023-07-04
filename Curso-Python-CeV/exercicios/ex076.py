#  Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#  No final, mostre uma listagem de preços, organizando os dados em forma tabular.

from tabulate import tabulate


produtos = [['Condicionador --------', 23,], 
             ['Shampoo --------', 25,],  
              ['Secador --------', 109,],
              ['Pinça --------', 17]]

for p in produtos:
    print(f'{tabulate(produtos)}')


# Jeito do professor:  como os nomes dos produtos estao sempre em posição par e os produtos em posição impar, se for divisivel por 2 mostra o nome do produto
# que seria impar, e se nao for, mostra o outro, dai é so botar um if na direita e outro na esquerda

tatuagem = ('Agulha', 3.00,
            'Batoque', 3.00,
            'Tinta', 40.00,
            'Carbono', 10.00,
            'Luva', 20.00,
            'Vaselina', 10.00)

for posicao in range(0, len(tatuagem)):   #pra cada posição na tupla tatuagem, contar de 0 até o tamanho da tupla 
    if posicao % 2 == 0:
        print(f'{tatuagem[posicao]:.<30}')
    else:
        print(f'{tatuagem[posicao]:.>30}')
