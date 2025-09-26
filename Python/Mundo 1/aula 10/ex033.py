numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
numeros = [numero1, numero2, numero3]
menorNumero = min(numeros)
maiorNumero = max(numeros)
print(f"\nOs números digitados foram: {numero1}, {numero2}, {numero3}")
print(f"O menor número é: {menorNumero}")
print(f"O maior número é: {maiorNumero}")