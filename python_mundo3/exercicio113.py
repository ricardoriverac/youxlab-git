def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print (f'''ERROR
tente novamente''')
            continue
        else:
            return n
        
num = leiaint('Digite um valor: ')
print (f'O valor foi {num}')