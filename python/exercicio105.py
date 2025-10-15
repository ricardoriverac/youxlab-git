def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['madia'] = sum(n)/len(n)
    if sit:                                             
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)

# n = int(input('Digite uma nota: '))
# for c in n:
#     print(n)

#     def teste(b):
#     global a # global - por favor não use crie uma variavel 'A' use o a global  
#     a=8
#     b+=4 # soma com o de fora
#     c=2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
# # Programa principal
# a=5
# teste(a)
# print(f'A dentro vale {a}')