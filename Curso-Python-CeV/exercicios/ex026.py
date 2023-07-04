# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "E"
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. 

# strip() tira os espaços

frase = str(input('Digite a frase: ')).lower().strip()
qt = frase.count('e')
qt2 = frase.find('e')+1
qt3 = frase.rfind("e")+1
print(f'Nessa frase, a letra e aparece {qt} vezes')
print(f'Nessa frase a letra e aparece pela primeira vez na posição: {qt2}')
print(f'Nessa frase a letra e aparece pela ultima vez na posição {qt3}')
print('='*20)


#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# DICA: - COUNT - FIND - RFIND


q = str(input('PUT A QUESTION RIGHT HERE')).upper().strip()

first = q.count('A')   #Quantas vezes
sec = q.find('A') +1   #Em que posição
l = q.rfind('A')  +1    #Em que posição aparece a última vez    

print(f'A letra > A < aparece {first} vez(es) na frase')
print(f'Pela primeira vez na {sec}º posição')
print(f'E pela última vez na {l}º posição')

# ponto de parada

r = 'S'

while r == 'S':
    numero = int(input('Digite um número'))
    r = str(input('Quer continuar [S/N]')).upper()

print('FIM')
