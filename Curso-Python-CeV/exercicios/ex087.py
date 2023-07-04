# Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.


matriz = [[], [], []]

p = c3 = 0  

for c in range(3):
    for y in range(3):
        matriz[c].append(int(input(f'Digite um valor para posição [{c},{y}]: ')))
        p += matriz[c][y] if matriz[c][y] % 2 == 0 else 0        #Peguei a dica de botar tudo junto pra reduzir codigo
        c3 += matriz[c][y] if y == 2 else 0
print('-' * 35, *matriz, sep='\n')  # Mostra a matriz   #\n quebra a linha #sep= define um caractere de separação
print('-' * 35, f'\nA soma dos números pares é {p}')
print(f'A soma dos números da terceira coluna é {c3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
