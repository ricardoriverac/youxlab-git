import math

def is_prime(number):
   
    if number < 2:
        return False
   
    if number == 2:
        return True
   
    if number % 2 == 0:
        
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False  


numero_para_verificar = int(input("Digite um número para verificar se é primo: "))

if is_prime(numero_para_verificar):
    print(f"{numero_para_verificar} é um número primo.")
else:
    print(f"{numero_para_verificar} não é um número primo.")