numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove' ,
             'dez', 'onze', 'doze', 'treze', 'catorze', 
            'quinze', 'dezesseis', 'dezessete', 'dezeito', 
            'dezenove', 'vinte')

numero = int(input("Digite um numero entre 0 e 20: "))
print(f"O numero {numero} por extenso é {numeros_extenso[numero]}")