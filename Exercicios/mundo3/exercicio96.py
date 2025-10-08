def area(largura, comprimento):
  """
  Calcula e exibe a área de um terreno retangular.

  Args:
    largura: A largura do terreno.
    comprimento: O comprimento do terreno.
  """
  area_calculada = largura * comprimento
  print(f"A área do terreno é: {area_calculada} metros quadrados.")

largura_terreno = float(input("Digite a largura do terreno em metros: "))
comprimento_terreno = float(input("Digite o comprimento do terreno em metros: "))

area(largura_terreno, comprimento_terreno)