from time import sleep
c = ('\033[m',               # 0 - sem cores
     '\033[0;30;41m',        # 1 - vermelho
     '\033[0;33;42m',        # 2 - verde
     '\033[0;30;43m',        # 3 - amarelo
     '\033[0;30;44m',        # 4 - azul
     '\033[0;30;45m',        # 5 - roxo
     '\033[7;30m',           # 6 branco
     )
def ajuda(coman): #Recebe o nome de um comando (coman) que você digitou.    
    titulo(f'Acessando o manual do comando \'{coman}\'', 4) #Mostra um título azul dizendo "Acessando o manual do comando..."

    print(c[6], end='') #Usa c[6] (cor branca invertida) pra destacar o texto do help.

    help(coman) #Mostra a ajuda do Python usando help(coman)

    print(c[0], end='') #Depois volta para a cor normal 

    sleep(2) #espera 2 segundos.

def titulo(msg, cor=0):     #Essa função mostra uma mensagem com bordas e cor, tipo um título.
                            #O cor=0 significa que, se você não escolher cor, ele mostra sem cor mesmo.
                            
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('-'*tamanho)
    print(f' {msg}')          
    print('-'*tamanho)
    print(c[0], end='')

    sleep(1) #O sleep(1) dá uma pequena pausa de 1 segundo, só pra deixar o programa mais “suave”.

#PROGRAA PRINCIPAL
comando = ''
while True: #Fica repetindo enquanto você não digitar FIM.
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("FUNÇÃO ou BIBLIOTECA > ")) #Cada vez, mostra o título principal e pede pra você digitar algo.

    if comando.upper() == 'FIM': #Se digitar FIM, ele mostra "ATÉ LOGO!" em vermelho e termina.
        break
    else:
        ajuda(comando) #Se digitar qualquer coisa (tipo print, len, math...), ele mostra o help().
        
titulo('ATÉ LOGO!', 1)
