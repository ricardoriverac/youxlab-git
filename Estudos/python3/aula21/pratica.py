
def contador (i,f,p):
    """

    -> Faz uma contagem e mostra na tela 
          :parametro i: inicio da contagem
          :parametro f: fim da contagem
          :parametro p: passo da contagem
          :return: sem retorno
          Função criada por Peter Cout
          """
    c=i
    while c<=f:
        print(f'{c}', end='..')
        c+=p
    print('FIM')

contador(2,10,2)


def teste():
    n=n

n=2
print(f'No app n vale {n}')
def teste(b):
    global a
    a=8
    b = b + 4 
    c=2
    print(f'A variavel b tem valor {b}')
    print(f'A variavel c tem valor {c}')
    print(f'A variavel a tem valor {a}')


a=5
teste(5)
# def somar(a=0, b=0, c=0):
#     s= a+b+c
#     print(f'A soma vale {s}')

# somar(3,2,8)
# somar(2,2,2)
def somar (a=0, b=0, c=0):
    s=a+b+c
    return s

r1=somar(3,2,8)
r2=somar(4,5,7)
r3= r1+r2

print(f'O resultado das duas somas são {r3}')

def fatorial (num=1):
    f=1
    for c in range (num, 0, -1):
        f*=c
    return f
n= int(input('Digite seu numero fatorial :'))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

def par (n=0):
    if n % 2 == 0:
        return True
    else: 
        return False
num = int(input('Digite um numero para verificação '))
if par(num):
    print(f'é par!')
else:
    print('Não é par')