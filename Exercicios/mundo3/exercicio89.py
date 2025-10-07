lista = list()

while True:
    nome = str(input("Qual seu nome?: "))
    nota_1 = float(input("Digite sua 1ª nota: "))
    nota_2 = float(input("Digite sua 2ª nota: "))
    media = (nota_1 + nota_2) / 2
    lista.append([nome, [nota_1, nota_2], media])
    resposta = str(input("Deseja continuar? [S/N]: ")).upper()
    if resposta in "N":
        break

print(f'{"Nome":<10}{"Média":>8}')

for i, c in enumerate(lista):
    print(f"{i:<4}{c[0]:<10}{c[2]:>8.1f}")
while True:
    opcao = str(input("Qual aluno deseja ver? [fim:para parar o codigo]: "))
    if opcao == "fim":
        print("Finalizado!")
        break
    opcao = int(opcao)
    if opcao <= len(lista) -1:
        print(f"As notas de {lista[opcao][0]} são {lista [opcao][1]}")