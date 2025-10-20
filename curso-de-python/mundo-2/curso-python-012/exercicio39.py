from datetime import datetime
ano_atual = datetime.now().year
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento
print(f'Você tem {idade} anos.')
if idade < 18:
    tempo_restante = 18 - idade
    print(f'Você ainda vai se alistar. Faltam {tempo_restante} ano(s) para o seu alistamento.')
elif idade == 18:    
    print('Já é a hora exata de se alistar ao serviço militar.')
else:
    tempo_atrasado = idade - 18
    print(f'Já passou do tempo do alistamento. Você está atrasado há {tempo_atrasado} ano(s).')