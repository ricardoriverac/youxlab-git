def escreva(mensagem):
    tamanho = len(mensagem) + 4 
    print('~' * tamanho)
    print(f'{mensagem}')
    print('~' * tamanho)

escreva('Caio Dantas')
escreva('Desafio Python')