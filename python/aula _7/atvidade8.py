preço = float(input("qual eo preço do produto? R$")) 
novo = preço - (preço * 5/ 100)
print(f"O produto que custava R${preço}, na promoçao com desconto de 5% vai custa R${novo:.2f}")