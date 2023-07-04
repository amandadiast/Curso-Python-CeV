#  Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#  No final, serão exibidos todos os valores únicos digitados, em ordem crescente

lst = []
question = ''

while True:
    fornow = int(input('Digite um número ou digite 999 para encerrar'))
    if fornow in lst:
        print('O número digitado já está na lista')
    else:
        lst.append(fornow)
    if fornow == 999:
        break

lst.sort()
print(lst)