# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
from urllib import request

#cria tratamento de exceção

try:
    site = urllib.request.urlopen('http://www.facebook.com')   #tentar abrir uma url
except urllib.error.URLError:   #exceção padrão
    print(f'O site não está acessivel no momento')
else:
    print('Tudo ok')

    #site.read()   = le o conteudo do site