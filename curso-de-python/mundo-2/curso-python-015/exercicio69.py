
resposta = "S"
contMais18 = 0
contHomems = 0
contMulheresMenos20 = 0
while resposta == "S":
    idade = int(input("idade: "))
    sexo = str(input('digite seu sexo [M/F]: '))
    if (idade >18):
        contMais18 = contMais18 + 1
        #contMais18 += 1
    if ( sexo == "M"):
        contHomems += 1
    else: 
        if (idade <20):
            contMulheresMenos20 += 1





    
    resposta = str(input(f'voce deseja continua? [S/N]: ')).upper()