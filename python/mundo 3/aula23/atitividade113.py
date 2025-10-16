def leiaint(msg):
    while True:
        try:
            entrada = int(input(msg))
        except(ValueError,TypeError):
         print("ERRO:por favor,digite um numero valido ")
         continue
        except KeyboardInterrupt:
         print("Entrada de dados interrompida pelo usuário.")
         return 0
        else:
         return entrada
         
 

numero = leiaint("digite um numero: ") 
print(f"voce digitou o numero {numero}")          

