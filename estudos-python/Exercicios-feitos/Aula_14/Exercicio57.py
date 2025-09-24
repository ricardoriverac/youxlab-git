sexo = input('Qual o seu sexo?:\n[M] para Masculino e [F] para Feminino:').upper()
while sexo != 'M' and sexo != 'F':
    print ('Você não escolheu nenhuma das opções! Corrija')
    sexo = input('Qual o seu sexo?:\n[M] para Masculino e [F] para Feminino:')
print('Obrigado por responder!')