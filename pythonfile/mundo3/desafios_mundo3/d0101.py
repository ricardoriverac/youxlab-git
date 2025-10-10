from datetime import date

def voto(idade):
  if idade < 16:
       
       return (f'Voce tem {idade} anos, você não pode votar')
  elif 16 >= idade < 18 or idade > 65:
        
        return (f'Voce tem {idade} anos, seu voto é opicional')
  elif idade >= 18:
        return (f'Voce tem {idade} anos, seu voto é obrigatorio')

        
ano = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print(voto(idade))