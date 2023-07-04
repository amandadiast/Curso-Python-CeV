#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

mvelho = 0
medidade = 0
mulher = 0
somaidade = 0
for pessoa in range(1, 5):
    n = str(input(f'Nome da {pessoa} pessoa'))
    i = int(input(f'Idade da {pessoa} pessoa'))
    s = str(input(f'Sexo da {pessoa} pessoa: [M/F]')).strip().upper()
    somaidade += i
    if pessoa == 1 and s == 'M':
        mvelho = i
        nmvelho = n
    if i > mvelho and s == 'M':
        mvelho = i
        nmvelho = n
    if s in 'F' and i < 20:
        mulher += 1
medidade = somaidade / 4
print(f'A média de idade é: {medidade} e a idade do mais velho é {mvelho}, sendo que seu nome é {nmvelho} e tem {mulher} mulheres com menos de 20 anos')


# JEITO 2 

RED = '\033[1;31m'
NORED = '\033[0m'
hmaisvelho = 0
nomevelho = ''
totalidade = 0
mulheres = 0
media = 0

for pessoa in range(1, 5):
    nome = str(input(f'Qual o nome da {pessoa} pessoa? '))
    idade = int(input(f'Qual a idade da {pessoa} pessoa? '))
    genero = str(input(f'Qual o genero da {pessoa} pessoa? ')).upper()
    totalidade += idade
    if pessoa == 1 and genero in 'M':
        hmaisvelho = idade
        nomevelho = nome
    if idade > hmaisvelho and genero in 'M':
        hmaisvelho = idade
        nomevelho = nome
    if genero in 'F' and idade < 20:
        mulheres += 1
media = totalidade / pessoa

print(RED + f'O homem mais velho se chama {nomevelho} e sua idade é de {hmaisvelho} anos, a média de idades é de {media:.2f} anos e {mulheres} mulheres tem menos de 20 anos', end=' ' + NORED)


