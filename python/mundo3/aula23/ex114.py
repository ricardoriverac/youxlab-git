#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('Não consegui acessar.')
else:
    print('Consegui acessar.')