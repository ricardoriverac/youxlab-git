from datetime import date
ano_atual= date.today().year
print(ano_atual)
anoNascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - anoNascimento
anos_passados= idade - 18

if idade<18:
    print('Você está preste a se alistar.')
elif idade==18:
    print('Já está na sua hora de se alistar.')
else:
    print(f"Ja se passaram {anos_passados} anos, você não pode mais!")