numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','desenove','vinte')
while True:
 opcao = int(input('Digite um numero: '))
 if 0 <= opcao <= 20:
  print(f'Voce digitou o numero {numeros[opcao]}')
  continuar = str(input('Voce quer continuar [S/N]?'))
  if continuar not in 'Ss':
   break
