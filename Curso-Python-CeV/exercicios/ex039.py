#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# prazo para se alistar: pessoas com até 18 anos

print('~' * 20)
nasc = int(input('Qual é o seu ano de nascimento?'))
print('~' * 20)

calc = 2023 - nasc

if calc <= 18:
    print('Você ainda pode se alistar')
else:
    print(f'Não da mais tempo para se alistar pois você tem {calc} anos.')


# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# tq = texto qualquer


def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


escreva('Amanda')
