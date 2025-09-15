nomeCompleto = (input('Digite o seu nome completo: '))
listaNomes = nomeCompleto.split()
primeiroNome = listaNomes[0]
ultimoNome = listaNomes[-1]
print('Seu primeiro nome é {}'.format (primeiroNome))
print('Seu ultimo nome é {}'.format (ultimoNome))