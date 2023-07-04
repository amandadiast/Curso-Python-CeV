# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


n1 = int(input('Digite um número:  '))
n2 = int(input('Digite outro número: '))

escolha = 0

while escolha != 5:
    print('''   * ESCOLHA UMA OPÇÃO:    
 [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa''')
    escolha = int(input('QUAL A SUA ESCOLHA?  '))
    if escolha == 1:
            soma = n1 + n2
            print(f'A soma entre {n1} e {n2} é: {soma}')
    elif escolha == 2:
            mult = n1 * n2
            print(f'A multiplicação entre {n1} e {n2} é: {mult}')
    elif escolha == 3:
            if n1 > n2:
                print(f'{n1}')
            else:
                print(f'{n2}')
    elif escolha == 4: 
            n1 = int(input('Digite um número:  '))
            n2 = int(input('Digite outro número: '))
        
    else:
            print('OBRIGADO! ADEUS...')

