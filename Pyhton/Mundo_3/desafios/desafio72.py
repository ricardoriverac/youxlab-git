numerosExtensos = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis",
    "sete", "oito", "nove", "dez", "onze", "doze", "treze",
    "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
    "dezenove", "vinte"
)
numero = int(input('escolha um número aleatório entre 0 e 20: '))
while numero < 0 or numero >20:
    numero = int(input('escolha um número aleatório entre 0 e 20:  '))

print(numerosExtensos[numero])