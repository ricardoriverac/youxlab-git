#for c in ranger(1-10):
  #if moeda
     #pega # condiacao do if 
   #passo # dentro do for, vai ser repetido 
   #pula
#passo #esta fora 
#vai fazer o contador no intervalo de 1 ate 10
for c in range(1,100): #vai fazer o contador no intervalo de 1 ate 100
 print('Oi')
 for c in range(10, 0, -1):# o menos 1 faz com que o programa mostre em 'contagem regressiva'
      print (c)                 
print('FIM')# aparece somente uma vez,ele esta fora no for
n = int(input('Digite um numero: '))
for c in range(0, n+1): #vai contar de 0 ate o numero escolhido pela pessoa, o +1 faz com que o numero escolhido tambem apareca
   print(c)
print('FIM')

inicio = int(input('Inicio'))
fim = int(input('Fim'))
passo = int(input('Passo'))
for c in range(inicio, fim+1, passo): #vai contar de onde eu quiser,pulando 'casas'
   print(c)
print('FIM')