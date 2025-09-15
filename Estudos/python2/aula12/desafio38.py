primeiroNumero= int(input('Qual o primeiro numero inteiro? '))
segundoNumero= int(input('QUal o segundo numero inteiro?  '))
if primeiroNumero>segundoNumero:
    print(str('O primeiro número é maior que o segundo número! '))
elif segundoNumero>primeiroNumero:
    print(str('O segundo número é maior que o primeiro número! '))
elif primeiroNumero == segundoNumero:
    print(str('Não existe número maior, os dois são iguais'))