from modulos.interface import cabecalho
def arquivo_existe(nome):
    try:
        with open(nome,"rt"):
            pass
    except FileNotFoundError:
        return False
    else:
        return True
def criar_arquivo(nome):
    try:
        with open(nome, "wt+"):
            pass  
    except Exception as erro:
        print(f'ao criar o arquivo:{erro}\033[m ')    
    else:
        print(f'\033[32mArquivo "{nome}" criado com sucesso!')    
def ler_arquivo(nome):
    try:
        with open(nome, 'rt') as arquivo:
            cabecalho('PESSOAS CADASTRADAS')
            for linha in arquivo:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')
    except Exception as erro:
        print(f'\033[31mErro ao ler o arquivo: {erro}\033[m')


def cadastrar_pessoa(nome_arquivo, nome='desconhecido', idade=0):
    try:
        with open(nome_arquivo, 'at') as arquivo:
            arquivo.write(f'{nome};{idade}\n')
    except Exception as erro:
        print(f'\033[31mHouve um erro na hora de escrever os dados: {erro}\033[m')
    else:
        print(f'\033[32mNovo registro de {nome} adicionado com sucesso!\033[m')