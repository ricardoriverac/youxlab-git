#ler 3 retas para saber se elas podem formar um triângulo
print('-=-'*20, '\nAnalisador de Triângulos\n', '-=-'*20)
reta1 = float(input('reta 1: '))
reta2 = float(input('reta 2: '))
reta3 = float(input('reta 3: '))

print(f'podem formar um triângulo' if  reta1 < reta3 + reta2 and reta2 < reta3 + reta1 and reta3 < reta2 + reta1 else 'Não conseguem formar um triângulo')