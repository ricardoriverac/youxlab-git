from datetime import date
countMajorAge = 0
countMinorAge = 0
ano = date.today().year
for c in range(1, 8):
    digiteIdade = int(input('Digite o ano: '))
    idade = (ano - digiteIdade)
    
    if idade >= 18:
        countMajorAge += 1
    else:
        countMinorAge += 1
print(f'Você possui {countMajorAge} no grupo de maiores de idade \nVocê possui {countMinorAge} no grupo de menores de idade')