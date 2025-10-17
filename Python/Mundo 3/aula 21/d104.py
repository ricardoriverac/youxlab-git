print('-'*40)
print('     VALIDANDO ENTRADA DE DADOS:')
print()
def leiaInt(msg):
    ok = False # ok = False → Serve pra controlar o laço (while).
               # Quando for True, quer dizer que o valor digitado está certo.

    valor = 0 # Laço infinito que só para quando o número for válido.
    while True:
        num = str(input(msg)) #Pede pro usuário digitar algo, e guarda como texto (str).
                              #A mensagem que aparece é a que foi passada como msg.

        if num.isnumeric(): #Verifica se o que foi digitado é um número inteiro positivo (só com dígitos de 0 a 9).
                            #Se sim, continua o processo.

            valor = int(num)
            ok = True        # Converte pra int
                             #Marca ok = True pra sair do laço

        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m') #Se a pessoa digitou letra, espaço ou algo errado, mostra uma mensagem de erro em vermelho

        if ok:
            break # Se ok virou True, então o número foi aceito e o laço quebra (para).

    return valor #A função devolve o número inteiro validado.

#PROGRAA PRINIPAL
num = leiaInt('-- Digite um número: ') #Aqui você chama a função leiaInt() com a mensagem que vai aparecer pro usuário.

print(f'   Você digitou o número {num}.')
print('-'*40)

#ANOTAÇÕES:
#leiaInt()	  ->    Lê um número inteiro com verificação
#.isnumeric() ->    Verifica se o texto tem só números
#\033[0;31m	  ->    Cor vermelha no terminal (ANSI)
#while True	  ->    Repete até digitar certo
#return	      ->    Entrega o número final pro programa