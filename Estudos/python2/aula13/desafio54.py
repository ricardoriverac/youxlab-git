pessoasAnalisadas= int(input('Quantas pessoas serão analisadas? ').upper().replace('Pessoas', ''))
pessoas=0
pessoasMaiores=0
pessoasMenores=0
anoAtual= 2025
for c in range (1, pessoasAnalisadas+1):
    pessoas=pessoas+1
    idades= (int(input(f'Em qual ano a pessoa {pessoas} nasceu?')))
    pessoasIdades= anoAtual - idades
    if pessoasIdades > 18:
        pessoasMaiores=pessoasMaiores+1
    elif pessoas < 18:
        pessoasMenores = pessoasMenores+1
print(str(f'Temos {pessoasMaiores} pessoas maiores de idade\n E também {pessoasMenores} pessoas menores de idade'))