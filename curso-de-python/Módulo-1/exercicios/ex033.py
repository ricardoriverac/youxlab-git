primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))
terceiroNumero = int(input('Digite o terceiro número: '))
menor = primeiroNumero
if segundoNumero < primeiroNumero and segundoNumero < terceiroNumero:
    menor = segundoNumero
if terceiroNumero < primeiroNumero and terceiroNumero < segundoNumero:
    menor = terceiroNumero
maior = primeiroNumero
if segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
    maior = segundoNumero
if terceiroNumero > primeiroNumero and terceiroNumero > segundoNumero:
    maior = terceiroNumero
print(f'O menor número é o número {menor}.')
print(f'O maior número é o número {maior}.')