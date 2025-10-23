def leiaInt(mensagem):
    numero_lido = input(mensagem)
    
    
    if numero_lido == '':
        print("ERRO: Nenhum valor informado")
        return
    if  not numero_lido.isnumeric():
        print("ERRO: Foi digitado caracter não numérico")
        return
    
    return int(numero_lido)
    


        
        
        
num = leiaInt("Digite um número inteiro: ")
print(num)