#Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(texto):
    tamanho = len(texto) + 3
    decora = '-' * tamanho
    print(decora)
    print(f' {texto}')
    print(decora)
escreva('TENHA UMA BOA TARDE!')
escreva('Nada compra seu esforço.')
escreva('O caminho está somente começando.')
