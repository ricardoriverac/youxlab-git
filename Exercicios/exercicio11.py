largura=float(input("Digite a largura da sua parede em metros: "))
altura=float(input("Digite a altura da sua parede: "))
area=largura*altura
litrosDeTinta=27
conversao=area/litrosDeTinta
print(f"A area {area} e usamos {conversao} litros de tinta")