
from datetime import date
atual = date.today().year
menor = 0
maior = 0
for pess in range(1, 8):
    nasc = int(input('em que ano a {} pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade  >= 18:
         menor += 1
    else:
         maior += 1  
        
print(f"ao todo tivemos {menor} pessoas maiores de idade ") 
print(f"e tambem tivemos {maior} pessoas menores de idade ")       
