#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#- Quantidade de notas = qtnotas
#- A maior nota  = man
#- A menor nota   = men
#- A média da turma  = media
#- A situação (opcional)  = sit

#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

lst = []
n = []
q = []

def notas ():
    """ Quantidade de notas = qtnotas
    A maior nota  = man
    A menor nota   = men
    A média da turma  = media 
    A situação (opcional)  = sit"""
    validation = 'S'
    qtnotas = int(input(f'Quantas notas de cada aluno você quer cadastrar?'))
    q.append(qtnotas)
    while validation == 'S':
        for c in range(qtnotas):
            nota = float(input(f'nota nº {c + 1}: '))
            n.append(nota)
        validation = input(f'Quer adicionar mais um aluno com a quantidade: {qtnotas} de notas?? [S/N]?   ').upper()
    man = max(n)
    men = min(n)
    media = sum(n)/len(n)
    total = len(n)
    if media > 7:
        situacao = 'boa'
    elif media < 7:
        situacao = 'ruim'
    turma = dict()
    turma['maior nota'] = man
    turma['menor nota'] = men
    turma['media'] = media
    turma['total'] = total
    turma['situacao'] = situacao
    print(f'Foi cadastrado {q} notas de cada aluno. A maior nota foi da turma foi {man}, a menor foi {men}, a média foi {media:.2f} e a quantidade total de notas foi {total}')
    print(turma)

help(notas)
notas()


#jeito do professor
#def notas (*n, sit=False)
# r = dict{}
# r['total'] = len(n)
# r['maior'] = max(n)
# r['menor'] = min(n)
# r['média] = sum(n)/len(n)
#if sit:
#    if r['média'] > 7:
#        r['situação'] = 'boa'
#    elif r['media'] >=7:
#        r['situação'] = 'média'
#    else:
#        r['situação'] = 'ruim'
#return r