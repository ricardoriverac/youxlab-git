e = 4
while e == 4 :
    v1 = int(input('Digite um primeiro valor: '))                            #valor 1
    v2 = int(input('Digite um terceiro valor: '))                            #valor 2
    print ('''escolha uma operação
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa''')
    e = int(input(''))
    if e == 1 :
        sdv = v1 + v2                                                         #soma dos dois valores
        print ('você escolheu a opção [1], a soma dos dois valores é {}' .format(sdv))
    if e == 2 :
        mdv = v1 * v2                                                        #multiplicação dos dois valores
        print ('você escolheu a opção [2], a multiplicação dos dois números é {}' .format(mdv))
    if e == 3 :
        if v1 > v2 :
            print ('você escolheu a opção [3], o número {} é maior que o número {}' .format(v1, v2))
        else :
            print ('você escoçheu a opção [3], o número {} é maior que o número {}' .format(v2, v1))
    if e == 5 :
        print ('você escolheu a opção [5], você deseja sair do programa :( ')
        pass