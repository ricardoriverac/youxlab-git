def fatorial (num=1, show=False):
    """fatorial(n,show=false)
           -> Calcula o fatorial de um número.
              :param num: o numero a ser calculado
              : param show: (opcional) Mostrar ou não a conta
              : param return: o valor do Fatorial é um número n"""
    operacao=[]
    ocultamento=str(input('Escolha se quer ver apenas o resultado final ou a operação completa [RF/O]').upper())
    f=1
    for c in range (num, 0, -1):
        f*=c
        operacao.append(f"{c}")
    if ocultamento == 'O':
        resultado = f"{' x '.join(operacao)}"
        return f"{resultado} = {f}"

    else:
        return f
n=int(input('Escolha seu numero fatorial: '))
print(f'O resultado da fatoração de {n} é {fatorial(n)}')