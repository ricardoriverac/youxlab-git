print('Gerador de PA')
print('-=' * 10)
contador = 0

primeiroTermo = int(input('Primeiro Termo:'))
razao = int(input('Razão da PA:'))
termo = int(input('quantos termos você quer ver?:'))


while contador < termo:
    conta = primeiroTermo + contador * razao
    print(conta, end='->')
    contador += 1
    

print('FIM')