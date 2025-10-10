
produtosCadastrados= list()
while True:
    sistema=int(input('Qual opção do menu você deseja selecionar?'))
    """[1] Cadastrar produto
       [2] Listar produtos
       [3] Buscar produto
       [4] Atualizar estoque
       [5] Remover produto
       [6] Sair"""
    if sistema == 1:
        produtosCadastrados.append(str(input('Digite o nome do produto para cadastro: ')))
        produtosCadastrados.append(float(input('Digite o preço do produto para cadastro: ')))
        produtosCadastrados.append(int(input('Digite a quantidade do produto para cadastro: ')))
    continuacao= str(input('Você deseja continuar usando o sistema? [S/N] '))
    if continuacao in 'Nn':
        print('Obrigado por usar o programa! Volte sempre!')
    elif continuacao not in 'Ss' or    'Nn'

     
    if continuacao in 'Nn':
        print('Obrig')
