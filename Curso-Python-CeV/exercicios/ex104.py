#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, 
#só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')



def titulo(msg):
    size = len(msg) + 4
    print('~'* size)
    print(f'  {msg}')
    print('~'* size)

def leiaInt(n=0):
    if n.isnumeric():
        return 'Obrigada'
    else:
        if n.isalpha():
            return 'Não é um número, apenas aceito valor numérico'


titulo('EXERCICIO 104')
n1 = input('Digite um número:    >  ')

print(leiaInt(n1))