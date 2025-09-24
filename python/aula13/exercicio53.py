frase = str(input('Digite uma frase: ')).strip().upper().split()
junta = ''.join(frase)
inverso = ''
for letra in range(len(junta) - 1, -1, -1):
    inverso += junta[letra]
print(inverso)
print(f'{junta}')
if inverso == junta:
    print('\033[33mEle é um palíndromo')
else:
    print('\033[31mEle não é um palíndromo')

#junta = ''.join(frase) define que o objeto 'frase' terá seus espaços apagados e será concatenado para uma nova string junta
#inverso = '' define um objeto com valor de string vazio, que será preenchido posteriormente
#for letra in range(len(junta) - 1, -1, -1)... Vamos por partes
#len(junta) - 1 lê a largura da string, ou seja, conta quantos caractéres a string possui, para depois transformar ela numa tradução em dígitos dessa quantidade
#depois, tem seu último caractere subtraído para uma melhor tradução da string
#após isso, o range define que irá ler até o último caracter, sendo ele -1 e define a condiçãod e lê-lo ao contrário, pelo dígito -1 
#assim, você adiciona essa string ao valor do objeto 'inverso', depois é só fazer a validação com if e else
