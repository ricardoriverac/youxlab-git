def escreva():
    texto = str(input('Digite um texto: ')).upper()
    tama = len(texto)
    print (f'=' * tama)
    print (f'{texto}')
    print (f'=' * tama)
escreva()