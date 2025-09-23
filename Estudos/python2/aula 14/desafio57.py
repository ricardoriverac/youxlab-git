PerguntaSexualidade= str(input('Qual sua sexualidade? [M ou F]')).upper().strip()
while PerguntaSexualidade not in 'MF':
    print('Por favor redigite seu sexo novamente! [M ou F]')
    print(str(input('Qual sua sexualidade? [M ou F]')))
print(f'Sexo {PerguntaSexualidade} registrado com sucesso')

