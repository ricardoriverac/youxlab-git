for pares in range(0, 51):
    print('.', end= '')
    if pares % 2 ==0:
        print(f'{pares}', end=' ')
print('acabou')
#nessa solução, a linha 2 exerce um objetivo específico: mostrar a quantidade de laços feitos para mostrar o resultado

for pares in range(0, 51):
    print('.', f'{pares}', end=' ')
print('acabou')
#nessa outra solução, são usados apenas um laço
#sendo uma solução mais rápida