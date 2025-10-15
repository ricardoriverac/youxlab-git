def escreva(txt):
    bora = len(txt) + 4
    print('~' * bora)
    print(f'{txt:^{bora}}')
    print('~' * bora)


escreva('Oi')
escreva('STUDIO X')
escreva('Exercício 97')
escreva('Curso py')