def leiaInt(mensagem):
    
    numeros=0
    while type(numeros):
        try:    
            numeros = int(input(mensagem))
        except (ValueError, TypeError):
            print("Erro: Entrada invalida! Digite um  número inteiro.")
            continue
    if numeros == int:
        print('Obrigado')    
    
    else:
        return numeros
    
    

leiaInt("Digite o proximo numero: ")
       
        
        