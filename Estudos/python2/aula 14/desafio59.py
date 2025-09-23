primeiroValor=float(input('Qual o primeiro valor à ser selecionado? '))
segundoValor= float(input('Qual o segundo valor à ser selecionado?  '))
Sistema = 0
while Sistema != 5:    
    Sistema=int(input("""Qual sistema de resolução você quer selecionar? '))
          [1] Soma
          [2] Multiplicar
          [3] Maior
          [4] Novos números
          [5] Sair do programa """))
    if Sistema <= 0 or Sistema >= 6:
        print('Por favor escolha as opções disponíveis [1 a 5]')
             
    if Sistema == 1:
        soma= primeiroValor + segundoValor
        print(f'A soma de  {primeiroValor} com {segundoValor} é {soma}')
    elif Sistema == 2:
        Multiplicação= primeiroValor*segundoValor
        print(f'O resultado da multiplicação entre {primeiroValor} e {segundoValor} é {Multiplicação}')
        
    elif Sistema == 3:
        if primeiroValor>segundoValor:
            maior=primeiroValor
        elif segundoValor>primeiroValor:
            maior= segundoValor
        print(f'Entre {primeiroValor} e {segundoValor} o maior valor é {maior}')
        
    elif Sistema == 4:
            primeiroValor= float(input('Por favor escolha um novo valor primário: '))
            segundoValor= float(input('Por favor escolha um novo valor secundário: '))
            Sistema= int(input(menu).strip())
            if Sistema == 1:
                soma= primeiroValor + segundoValor
                print(f'A soma de  {primeiroValor} com {segundoValor} é {soma}')
            elif Sistema == 2:
                Multiplicação= primeiroValor*segundoValor
                print(f'O resultado da multiplicação entre {primeiroValor} e {segundoValor} é {Multiplicação}')
            elif Sistema == 3:
                if primeiroValor>segundoValor:
                    maior=primeiroValor
                elif segundoValor>primeiroValor:
                    maior= segundoValor
                print(f'Entre {primeiroValor} e {segundoValor} o maior valor é {maior}')
            elif Sistema == 4:
                primeiroValor= float(input('Por favor escolha um novo valor primário: '))
                segundoValor= float(input('Por favor escolha um novo valor secundário: '))