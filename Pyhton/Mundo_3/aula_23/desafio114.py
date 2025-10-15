import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('Site nao acessivel !!')
else:
    print('Consegui acessar ! !')
    print(site.read())