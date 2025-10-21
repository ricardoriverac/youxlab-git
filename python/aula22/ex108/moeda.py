#MÓDULO:

def dobro(a):
	return print(f"O dobro de R${a} é R${a * 2:.2f}")
def metade(a):
	return print(f"A metade de R${a} é R${a /  2:.2f} ")

def aumentar(a):
	b = a * 10/100
	return print(f"Aumentando em 10%, temos R${b + a:.2f}") 


def porcento(n):
    porc = (n * 10) / 100
    valor = n + porc
    return valor

def porcentomenos(n):
    porc = (n * 10) / 100
    valor = n - porc
    return valor