#Exercício Python 073: Crie uma tupla preenchida com as 20 pessoas mais ricas do mundo, na ordem de colocação. Depois mostre:
#a) As 5 primeiros pessoas.
#b) Os últimos 4 colocados.
#c) Pessoas em ordem alfabética. 
#d) Em que posição está o Bill Gates


ricos = ('Zero', 'Elon Musk', 'Jeff Bezos', 'Bill Gates', 'Larry Ellison', 'Warren Buffet', 'Larry Page', 'Sergey Brin', 'Steve Palmer',
'Michael Bloomberg', 'Jim Walton', 'Mark Zuckerberg', 'Rob Walton', 'Charles Koch', 'Julia Koch', 'Alice Walton', 'Michael Dell',
'Phil Knight', 'Mackenzie Scott', 'Jacqueline Mars', 'John Mars')

print(f'As 5 primeiras pessoas mais ricas do mundo são homens, o nome deles é, em ordem: {ricos[0:5]}')
print(f'Os 4 ultimos colocados são: {ricos[-4:]}')
print('Bill Gates está na posição:', end=' ')
print(ricos.index('Bill Gates')) 



