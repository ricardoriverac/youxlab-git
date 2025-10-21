def leiaint(msg):
    while True:
        try:
          num = int(input(msg))
        except (ValueError,TypeError):
           print(f'O numero é INVALIDO por favor digite um numero inteiro valido')
           continue
        except KeyboardInterrupt:
           print('Entrada de dados interrompida pelo usuario')
           return 0
        else:
           return num




def linha(tam=35):
    return '-' * tam 



def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha()) 


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
        print(linha())
        opc = leiaint('Sua opcao: ')
        return opc
