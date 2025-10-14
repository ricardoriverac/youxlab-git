import datetime
def voto(n):
    if n >= 65:
        print('O voto não é obrigatório')
    if n >= 18 and n <= 64:
        print('O voto é obrigatorio')
    if n >= 16 and n <= 17:
        print('O voto não é obrigatório')
    if n < 16:
        print('Não precisa votar')

nascimento = int(input('Ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - nascimento
print(f'Com {idade} anos: ',end='')
voto(idade)