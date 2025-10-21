import urllib
import urllib.request

try:
     site = urllib.request.urlopen('https://www.pudim.com.br/')
except :
        print('Site inacessivel no momento')
else:
        print('consegui acessar o site  ')

