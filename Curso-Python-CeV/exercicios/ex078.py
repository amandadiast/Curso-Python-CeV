# LISTAS #



#LISTAS SÃO MUTAVEIS

# Adicionar elementos novos na lista
# lanche.append('bolo')

# Adicionar um elemento entre outros elementos
#lanche.insert(0, 'bolo')
#estou adicionando bolo na posição 0

# Para apagar elementos
#del lanche[3]  #pela chave
# ou lanche.pop(3)   #pela chave
#lanche.remove('bolo')  #por elemento

# Criar listas através de range
# lanches = list(range(4, 11))

#Botar em ordem
#valores = [5,4,7,2,1,4]
#valores.sort()


# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
lista = []
maior = 0
menor = 0
for count in range (0, 5):
    lista.append(int(input('Digite um número:   ')))
    if count == 0:
        maior = lista[count]        #lista na posição ''c''
        menor = lista[count]
    else:
        if lista[count] > maior:
            maior = lista[count]
        if lista[count] < menor:
            menor = lista[count]


    
print(lista)
print(f'O maior é {maior}, e o menor é {menor}')