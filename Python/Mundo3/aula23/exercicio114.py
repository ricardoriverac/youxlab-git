import urllib
import urllib.request

try:
     site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
        print('Acesso ao site inacessivel no momento!')
else:
        print('Acesso permitido ao site!')