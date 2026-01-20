import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')

except urllib.error.URLError:
    print('Site pudim não acessado!!')
else:
    print('Site pudim acessaso!!')