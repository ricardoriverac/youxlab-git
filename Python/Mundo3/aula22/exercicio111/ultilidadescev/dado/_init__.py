def leiaDinheiro(mensagem):
    valido = False
    while not valido:
        resposta = str(input(mensagem)).replace(',', '.').strip()
        if resposta.isalpha() or resposta == '':
            print(f'Erro: \"{resposta}\" é um preço inválido!' )
        else:
            valido = True
            return float(resposta)
        
def leiaInt(mensagem):
    i = False
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            i = True
        else:
            print("Digite um número inteiro válido!")
        if i:
            break
    return valor

def leiaFloat(mensagem):
    i = False
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = float(numero)
            i = True
        else:
            print("Digite um número válido!")
        if i:
            break
    return valor