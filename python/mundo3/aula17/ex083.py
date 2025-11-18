#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.

pilha = []
frase = input('Digite uma frase com parênteses: ')
for char in frase:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
         pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua frase foi digitada com parênteses corretamente.')
else:
    print('ERRO, certifique se sua frase foi digitada com parênteses corretamnete.')



