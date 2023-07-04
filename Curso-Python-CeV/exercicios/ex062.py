#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.



CRED1 = '\033[45m'
CEND2 = '\033[0m'

pt = int(input('Insira aqui o primeiro termo:  '))
r = int(input('Agora insira a razão: '))
total = 0
termo = pt
cont = 1
mais = 20

while mais != 0:
    total += mais
    while cont <= total:
        print(CRED1 + f'({cont}º)' + CEND2, end=' ')
        print(f'TERMO -> {termo}, ', end=' ')
        termo += r
        cont += 1
    print('PAROU')
    mais = int(input('Quantos termos a mais você quer?  '))
print('acabou')


