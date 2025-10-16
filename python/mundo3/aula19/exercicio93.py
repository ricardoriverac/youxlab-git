informaçõesJgdr={}
total=[]
informaçõesJgdr['nome']=str(input("Nome do jogador: "))
informaçõesJgdr['q/partidas']=int(input(f"Quantas partidas? "))
for g in range(informaçõesJgdr['q/partidas']):
    quantidade_de_gols=int(input(f'Quantos gols fez na partida? '))
    total.append(quantidade_de_gols)
    informaçõesJgdr['total']=total
    informaçõesJgdr['total']=sum(total)
print(f'O nome do jogador é {informaçõesJgdr["nome"]}')
print(f'O total de gols que {informaçõesJgdr["nome"]} fez foi {total}')    
print(f'A soma de todosos gols foi de {sum(total)}')