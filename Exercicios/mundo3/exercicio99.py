def maior(*numero):
    print(f'vendo os valores')
    if not numero:
        print("Não foram passados valores para analisar.")
        return None
    maior_valor = max(numero)
    print(f'O maior valor é {maior_valor}')
    return maior_valor

maior(2, 9, 4, 7, 1)
maior(1, 2)
maior(6)
maior()