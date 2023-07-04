# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 20 primeiros termos da progressão usando a estrutura while.


CRED1 = '\033[45m'
CEND2 = '\033[0m'

pt = int(input('Insira aqui o primeiro termo:  '))
r = int(input('Agora insira a razão: '))
any = 1

while any <= 20:
    print(CRED1 + f'({any}º)' + CEND2, end=' ')
    print(f'TERMO -> {pt}, ', end=' ')
    pt += r
    any += 1
