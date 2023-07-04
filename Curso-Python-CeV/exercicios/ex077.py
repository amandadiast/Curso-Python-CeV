#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
# só consegui vendo o video

t = ('Lupa', 'Almofada', 'Tênis', 'Abóbora', 'Lapela')

for cadapalavra in t:
    print(f'\nna palavra {cadapalavra} temos', end=' ')
    for cadaletra in cadapalavra:
        if cadaletra.lower() in 'aeiou':
            print(cadaletra, end=' ')