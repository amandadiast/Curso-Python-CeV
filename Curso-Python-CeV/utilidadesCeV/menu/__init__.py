pessoas_cadastradas = []

def vercadastro():
    print(pessoas_cadastradas)
    escolhacadastro = int(input('De quem você quer ver o cadastro'))

def cadastrar():
    v = 'S'
    while v == 'S':
        pessoas_cadastradas.append(input('Qual é o nome da pessoa? '))
        v = input('Quer cadastrar mais?  [S/N]:').upper()
def sair():
    print('FIM')

def menu():
    while True:
        try:
            print('CADASTRO DE PESSOA FISICA'.center(30))
            print('ESCOLHA UMA OPÇÃO:')
            print('1 - CADASTRAR NOVA PESSOA\n'
                  '2 - VER CADASTRO\n'
                  '3 - SAIR')
            escolha = int(input('>'))
        except(TypeError, ValueError):
            print('ERRO de tipo ou valor')
            break
        else:
            if escolha == 1:
                cadastrar()
            if escolha == 2:
                vercadastro()
            if escolha == 3:
                print('Obrigada por usar nosso programa.')
                break
            return escolha