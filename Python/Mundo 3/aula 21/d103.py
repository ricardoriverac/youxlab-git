print('-'*40)
print('       FICGA DO JOGADOR:')
print()

def ficha(jog='<desconhecido>', gol=0): # jog = '<desconhecido>' → se ninguém digitar o nome, usa isso.
                                        #gol = 0 → se ninguém digitar quantos gols, considera zero.

    print(f'   O jogador {jog} fez {gol} gol(s) no campeonato.')

#PROGRAMA PRINCIPAL
nomeJog = str(input('-- Nome do Jogador: '))
golsJog = str(input('-- Número de Gols: ')) # Aqui a variável 'golsJog' teve que ser convertida para o tipo str (string),
                                            # pois o método (.isnumeric()) só pode ser usado para str(string).
if golsJog.isnumeric():
    golsJog = int(golsJog)  # Se a pessoa digitou só números, converte pra int.
else:
    golsJog = 0    #Se não digitou número (ou deixou em branco), considera 0.

if nomeJog.strip() == '':   #Verifica se o nome do jogador foi deixado em branco (só espaços, ou nada).
                            #strip() remove os espaços do começo e do fim.

    ficha(gol=golsJog) # Se não tem nome, chama a função ficha() só com os gols, e usa o nome do jogador como: <desconhecido>.

else:
    ficha(nomeJog, golsJog) #Se o nome foi digitado, chama a função com o nome e os gols.

print('-'*40)