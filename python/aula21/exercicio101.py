from datetime import date
def voto(a = 0):
    idade = date.today().year - a
    if idade > 18:
        resp = 'OBRIGATÓRIO'
    elif 16 <= idade < 18:    
        resp = 'OPCIONAL'
    elif idade < 16:
        resp = 'NEGADO'
    print(f'Com {idade} anos:', end=' ')
    return resp


valor = int(input('Digite o ano em que você nasceu: '))
print(voto(valor), end=' ')

