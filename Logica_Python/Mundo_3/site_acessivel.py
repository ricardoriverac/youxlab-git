import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLERROR:
    print('O site Pudim consegue ter acesso.')
else:
    print('Consegui acessar o site Pudim!')
