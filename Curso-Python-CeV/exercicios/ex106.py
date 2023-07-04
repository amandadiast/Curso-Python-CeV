#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
#O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

def h():
    while True:
        print('Sistema de Ajuda do Python')
        fm = str(input('Função ou Biblioteca >  [FIM PARA ENCERRAR] ')).strip().lower()
        if fm == 'fim':
            print('FIM')
            return
        print(help(f'{fm}'))


h()


