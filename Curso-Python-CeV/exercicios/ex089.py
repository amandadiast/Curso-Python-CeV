# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


students = []

a = 0
while True:
    name = str(input('Nome:    '))
    n1 = float(input('FIRST GRADE:   '))
    n2 = float(input('SECOND GRADE:   '))
    media = (n1 + n2) / 2
    students.append([name, [n1, n2], media])
    validate = str(input('Wanna continue??  [Y/N]')).upper()
    if validate in 'N':
        break
 
print(f'{"NOME":>4} {"-":>4} {"MEDIA":>8}')
for x, y in enumerate(students):
    print(f'{y[0]:>4} {y[2]:>8}')


