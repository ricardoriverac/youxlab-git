print('-'*40)
print('       FUNÇÃO PARA VOTAÇÃO:')
print()
def voto(anoNascimento): #Aqui a gente está criando uma função chamada voto.
                         #Ela precisa de um ano de nascimento pra funcionar.
                         #(Esse valor vai vir quando o usuário digitar.)
    from datetime import date
    atual = date.today().year #Aqui a gente pega só o ano atual e guarda na variável atual.
                              #Se hoje é 2025, então atual = 2025.
    idade = atual - anoNascimento
    if idade < 16:
        return f'   Com idade {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65: #A pessoa tem entre 16 e 17 anos?
                                         #Ou ela tem mais de 65 anos?
                                         #Se sim, o voto é opcional!
        return f'   Com idade {idade} anos: VOTO OPCIONAL!'
    else:
        return f'   Com idade {idade} anos: VOTO OBRIGATÓRIO!'
    
nascimento = int(input('-- Em que ano você nasceu?: '))
print(voto(nascimento))
print('-'*40)