def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print (f'''ERROR
tente novamente''')
        except (KeyboardInterrupt):
            print (f'O usuario não digitou nada')
            continue
        else:
            return n
        
num = leiaint('Digite um valor: ')
print (f'O valor foi {num}')