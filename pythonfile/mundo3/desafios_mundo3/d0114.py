import urllib.request           # 1
import urllib.error             # 2

def verifica_site(url):        # 3
    # garante que o usuário possa digitar "pudim.com.br" sem esquema
    if not url.startswith(('http://', 'https://')):   # 4
        url = 'http://' + url   # 5
    try:                       # 6
        # abre a URL com timeout de 5 segundos; fecha automaticamente
        with urllib.request.urlopen(url, timeout=5) as resposta:  # 7
            print(f'Conseguimos acessar {url} (status: {resposta.getcode()})')  # 8
    except urllib.error.URLError as e:  # 9
        # URLError é lançado quando há problema de rede, DNS, timeout, etc.
        print(f'Não foi possível acessar {url}. Motivo: {e.reason}')  # 10
    except ValueError:          # 11
        # urlopen lança ValueError para URLs mal formadas
        print('Endereço inválido. Tente algo como: pudim.com.br ou https://www.exemplo.com')  # 12

if __name__ == '__main__':    # 13
    site = input('Digite o endereço do site (ex: pudim.com.br): ').strip()  # 14
    verifica_site(site)        # 15
