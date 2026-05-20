def leiadinheiro(msg):
    valido = False
    while not valido: # "Enquanto não for válido" ele vai ficar lendo o valor.

        entrada = str(input(msg)).replace(',', '.').strip() #Subistituindo todas as virgulas por pontos. E tira todos os espaços 

        if entrada.isalpha() or entrada == '': #Aqui testamos se ela esta vazio e se tiver espaços tiramos eles.
           #Se a variável é alfanumérico.

            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else: #Se a variável não for alfanumérico

            valido = True
            return float(entrada)

