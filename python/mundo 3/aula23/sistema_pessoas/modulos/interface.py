def linha(tam=42):
    return "-"*tam
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
def menu(opçoes):
    cabecalho("MENU PRINCIPAL")   
    for i,item in enumerate(opçoes,start=1):
        print(f"{i} - {item}")  
    print(linha())
    while True:
        try:
            opcao = int(input("digite sua opçao: "))
            if 1 <= opcao <= len(opçoes):
                return opcao
            else:
                print("digite uma opçao valida: ")
        except (ValueError,TypeError):
            print('digite um numero inteiro')  
        except KeyboardInterrupt:
            print("prefiriu nao digitar")     
            return len(opçoes)   
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))   
        except   (ValueError,TypeError):   
            print('digite um numero inteiro valido')
            continue
        except KeyboardInterrupt:
            print('entrada de dados interrompida pelo usario')
            return 0
        else:
            return n