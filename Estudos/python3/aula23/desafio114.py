import urllib
import urllib.request
try:
    site=urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'Deu erro!')
else:
    print(f'Deu certo! ')
    print(site.read())