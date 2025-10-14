# def maior(numero):#def definir uma funçao
#     print(f'vendo os valores')
#     if not numero:
#         print('nao foram passados valores par analisar')
#         maior_valor = max(numero)
#     print(f'O maior valor é {maior_valor}')
#     return maior_valor   
# maior(2, 9, 4, 7, 1)
# maior(1, 2)
# maior(6)
# maior()

def maior(*numeros):#usa * para aceitar vários argumentos
    print('Analisando os valores passados')
    
    if not numeros:  #verifica se nenhum valor foi passado
        print('Nenhum valor foi passado para analisar.')
        return None #sai da função sem erro
    
    print(f'Valores recebidos: {numeros}')
    
    maior_valor = max(numeros) #encontra o maior valor
    print(f'O maior valor é {maior_valor}')
    
    return maior_valor
