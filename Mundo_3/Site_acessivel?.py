import requests


def testsite(url):
    '''
    testar sites de internet
    :param url: endereço para teste ex: www.ninoseg.com.br
    :return: informação se está acessivel ou nao
    '''

    try:
        response = requests.get(f'http://{url}', timeout=5)
    except:
        print('Error 404: Page not found.')
    else:
        print('A página requisitada está acessível.')


while True:
    url = str(input('Digite um site: '))
    if url == "0":
        print('\033[30;41mObrigado volte novamente.\033[m')
        break
    else:
        testsite(url)
