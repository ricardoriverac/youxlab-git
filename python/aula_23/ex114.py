import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.instagram.com/')
except urllib.error.URLError:
    print('O site Instagram não está disponível no momento.')
else:
    print('Acessei o site Instagram com sucesso!')