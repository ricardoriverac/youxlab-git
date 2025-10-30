#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = float(input('Digite o primeiro termo da P.A: '))
razao = float(input('Digite a razaõ da P.A: '))
termo_atual = primeiro_termo
contador = 1
total = 0
acrescen = 10
while True:
  total = total + acrescen
  while contador <= total:
     print(f' {termo_atual}')
     termo_atual += razao
     contador += 1
  acrescen = int(input('Digite quantos termos você quer que mostramos a mais: '))
  if acrescen == 0:
        break
print('Você colocou a opção 0, chegamos ao fim do programa, até a próxima!')




