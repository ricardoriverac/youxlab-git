def leialnt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
            return n
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

numero = leialnt('Digite um número: ')
print(f'Você digitou o número: {numero}')
