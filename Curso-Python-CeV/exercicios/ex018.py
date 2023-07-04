# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# aq = angulo qualquer
import math

aq = float(input('Qual é o angulo?   >   '))
c = math.cos(math.radians(aq))
t = math.tan(math.radians(aq))
s = math.sin(math.radians(aq))
print(f'COSSENO - {c:.2f}, TANGENTE - {t:.2f}, SENO - {s:.2f}')




