import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/imgres?q=imagens%20pudim&imgurl=https%3A%2F%2Fcozinha365.com.br%2Fwp-content%2Fuploads%2F2025%2F02%2FPudim-de-Leite-Condensado-S-1024x1024.webp&imgrefurl=https%3A%2F%2Fcozinha365.com.br%2Freceitas%2Fpudim-de-leite-condensado-lisinho-e-perfeito%2F&docid=6V-vO8pR1Y9YuM&tbnid=sNs2YnY4UJuhGM&w=1024&h=1024&hcb=2')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')