def line(msg):
    print('<>' * 27)
    print(f'  SISTEMA DE AJUDA PyHELP')
    print('<>' * 27)
    print()
    help(msg)
    print('=' * 40)
    print(f'  {option.capitalize()}')
    print('=' * 40)
option=str(input('Function or library\n->')).strip()
while True:
        if option == 'FIM':
            print('Program ended successfully')
            break
        line(option)
        option=str(input('Function or library\n->')).strip()