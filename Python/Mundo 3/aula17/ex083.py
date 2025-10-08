# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
# Passos
# 0. ler a expressão como string
# 1. andar de letra em letra, da string que receber
# 2. quando achar um parenteses aberto conta ele
# 3. quando achar um parenteses fechado conta ele
# 4. compara os dois contadores se forma iguais a expressão esta com o numero correto de parenteses





    
expressao = input('Digite uma expressão: ')
count = 0

for c in expressao:
    if c == '(':
        count += 1
    elif c == ')':
        count -= 1
    
    if count < 0:
        break

if count == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')