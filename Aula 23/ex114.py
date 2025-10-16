import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.netflix.com/br/')
except urllib.error.URLError:
    print('O site Netflix não está disponível no momento.')
else:
    print('Acessei o site pudim com sucesso!')
    print(site.read())