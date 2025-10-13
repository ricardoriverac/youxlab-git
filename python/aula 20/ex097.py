def escreva(txt):
    bora = len(txt) + 4
    print('~' * bora)
    print(f'{txt:^{bora}}')
    print('~' * bora)


escreva('Oi')
escreva('Te desejo um ótimo dia')
escreva('Não esquece de beber aguá!')

