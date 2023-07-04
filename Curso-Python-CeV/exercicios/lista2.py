#Lista dentro de outra lista
#  [:] = CÓPIA 
#   .clear()  = limpa a lista, serve mto para copiar a lista 1 para a lista 2 e apagar a lista 1 por exemplo


alunos = []
alunos.append('Euzinha')
alunos.append(23)
secondalunos = []
secondalunos.append(alunos[:])
alunos[0] = 'João'
alunos[1] = 24
secondalunos.append(alunos[:])
print(secondalunos)

# ver item por estrutura 

alunos2 = [['Maciel', 23], ['José', 27], ['Murilo', 47], ['Luisa', 15]]

print(alunos2[0][1])
 #idade do maciel 

# Aprimorando visualização, por exemplo ver todos os nomes

for cadapessoa in alunos2:
    print(cadapessoa[0])

# Mostrar apenas pessoas com mais de 21 anos

maior = menor = 0
for cadapessoa in alunos2:
    if cadapessoa[1] >= 21:
            maior += 1
    else:
            menor += 1

print(f'São {maior} maiores de 21 e {menor} menores de 21.')


