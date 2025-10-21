from datetime import date
def voto(idade):
  if idade < 16:
       return (f'Voce tem {idade} anos .AINDA NAO PODE VOTAR')
  elif 16 >= idade < 18 or idade > 65:
        return (f'Voce tem {idade} anos VOTO OPCIONAL')
  elif idade >= 18:
        return (f'Voce tem {idade} anos VOTO OBRIGATORIO')

        


ano = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print(voto(idade))