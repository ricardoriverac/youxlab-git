# Curso Python #10 - Condições (Parte 1)

# PRIMEIROS COMANDOS DO CARRO PARA ANDAR
# carro.siga()
# carro.esquerda()
# carro.siga()
# carro.direita()
# carro.siga()
# carro.direita()
# carro.siga()
# arro.esquerda()
# carro.siga()
# carro.pare()

# CONDIÇÃO
# se carro.esquerda()   senão
# if carro.esquerda():  else:
# bloco True            bloco False
# bloco_v_ # verdadeiro 
# bloco_f_ # falso

# exemplo:
# tempo = int(input('Quantos anos tem o seu carro? '))
# if tempo <=3:
#     print('Carro novo')
# else:
#     print('Carro velho')
# print('--FIM--')

#simplificado
# tempo = int(input('Quantos anos tem o seu carro? '))
# print('carro novo'if tempo<=3 else'carro velho')
# print('--FIM--')

# PRÁTICA
# nome = str(input('Qual é o seu nome? '))
# if nome == 'Gustavo':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(nome))

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
nota3 = float(input('Digite a sua terceira nota: '))
nota4 = float(input('Digite a sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4
print(f'A sua média foi {media:.1f}')
if media >= 6.0:
    print('Sua média foi boa. PARABÉNS!')
else:
    print('Sua média foi ruim. ESTUDE MAIS DA PRÓXIMA VEZ!')
