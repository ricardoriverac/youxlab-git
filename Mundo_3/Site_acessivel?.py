import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLERROR:
    print('O site Pudim esta acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')