#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104
#incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
import emoji
from emoji import emojize
def titulo(msg):
    size = len(msg) + 4
    print('~'* size)
    print(f'  {msg}')
    print('~'* size)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;30;41m Problema de tipo ou valor de dados.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;30;41mUsuário não inseriu os dados \033[m')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;30;41m Problema de tipo ou valor de dados.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;30;41mUsuário não inseriu os dados \033[m')
        else:
            return n


titulo('EXERCICIO 113')

num = leiaInt('Digite um valor')
print(emoji.emojize('Obrigado(a), volte sempre que possível! :red_heart:'))