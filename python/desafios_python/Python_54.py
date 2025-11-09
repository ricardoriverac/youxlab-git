from datetime import date
anoAtual = date.today().year
maiorDeIdade = 0
menorDeIdade = 0


for i in range(1,8):
    anoDeNascimento = int(input('Em qual ano a {} pessoa nasceu?:'.format(i)))
    idade = anoAtual - anoDeNascimento
    

    if idade <= 18:
        menorDeIdade +=1 
    else:
        maiorDeIdade +=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maiorDeIdade))
print('E também tivemos {} pessoas menores de idade'.format(menorDeIdade))
       


