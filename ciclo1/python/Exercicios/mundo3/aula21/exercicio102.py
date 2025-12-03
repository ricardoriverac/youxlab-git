def fatorial(numero, mostrar_calculo=False):
    if numero < 0:
        print("Fatorial não definido para números negativos.")
        return None
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
            if mostrar_calculo:
                print(f"Iteração {i}: resultado atual = {resultado}")
        return resultado

print("Calculando o fatorial de 6, mostrando o processo:")
resultado_com_processo = fatorial(6, mostrar_calculo=True)
print(f"O fatorial de 6 é: {resultado_com_processo}\n")

print("Calculando o fatorial de 2, sem mostrar o processo:")
resultado_sem_processo = fatorial(4)
print(f"O fatorial de 2 é: {resultado_sem_processo}")

print("\nTentando calcular o fatorial de -3:")
fatorial(-3)