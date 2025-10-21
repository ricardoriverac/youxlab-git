#def linha(tam = 42):
 #   return '-' * tam

#def cabeçalho(txt):
 #   print(linha())
  #  print(txt.center(42))
   # print(linha())


def leiaInt(msg):
    while True:
        try:
            r = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro. Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuário não digitou valor.\033[m')
            return 0
        else:
            return r
        

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc 


  