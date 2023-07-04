#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# pt = primeiro termo
# r = razão

pt = int(input('Insira aqui o primeiro termo   >'))
r = int(input('Agora insira a razão    >'))
enesimo = pt + (10 - 1) * r    #10 pq quero o décimo termo, poderia ser outro como 20 por exemplo
termos = 0

for cont in range (pt, enesimo, r):
    print(cont, end=' ')