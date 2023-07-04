# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#  retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(a= 0):
    c = 2023 - a
    if c < 18:
        return  ('Seu voto não é obrigatório')
    elif c > 18:
        return  ('Seu voto é obrigatório')
    else:
        if c > 16 and c > 18:
            return ('Voto opicional')

ano = int(input('Qual é o seu ano de nascimento?'))

print(voto(ano))

