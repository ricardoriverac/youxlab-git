import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except:
    print("nao consegui acessar")   
else:
    print("consegui acessar")     