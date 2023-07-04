# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salario?'))

mais = salario + (salario *10 / 100)
menos = salario + (salario *15 / 100)

if salario >= 1250.00:
    print(f'Com o aumento de 10% você passa a ganhar: R${mais:.2f}')
else:
    print(f'Com o aumento de 15% você passa a ganhar: R${menos:.2f}')

    

    # OUTRA SOLUÇÃO -   ECONOMIZA LINHA
print('---'*20)
sal = float(input('OUTRA SOLUÇAO - Digite o salário do funcionário: R$ '))

print(f'O novo sálario do funcionário será R$ {sal * 1.10 if sal > 1250 else sal * 1.15:.2f}')
