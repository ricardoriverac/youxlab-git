anoNascimento = int(input('Digite quantos anos você tem: '))
tempoAlistar = 17 - anoNascimento
tempoAlistamento = anoNascimento - 17
if anoNascimento < 17:
    print(f'Você tem {anoNascimento} anos, faltam {tempoAlistar} para você fazer o alistamento.')
elif anoNascimento == 17:
    print(f'Você tem {anoNascimento} anos, está na idade para se alistar!')
elif anoNascimento > 18:
    print(f'Você tem {anoNascimento} anos, já passou {tempoAlistamento} do seu tempo de alistamento.')