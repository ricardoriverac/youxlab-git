preço = float(input("preço das compras: R$ "))
print(""" formas de pagamento
[1] a vista dinheiro/cheque
[2] a vista no cartao
[3] 2* no cartao
[4] 3* ou mais no cartao""")
opçao = int(input("qual e a opçao"))
if opçao == 1:
    total = preço -(preço * 10 / 100 )
elif opçao == 2:
    total = preço - (preço * 5 / 100)    
elif opçao == 3:
        total = preço
        parcela = total / 2
        print(f"sua compra vai ser parcelada em 2x de R${parcela:.2f}")
elif opçao == 4: 
     total = preço + (preço * 20 / 100) 
     totalparç = int(input("quantas parcelas? "))
     parcela = total / totalparç
     print(f"sua compra sera parcelada em {totalparç}x de R${parcela:.2f} com juros ")
else: 
     total = preço
     print("opçao invalida de pagamento")        
print(f" sua compra de R$ {preço:.2f} vai custar R${total:.2f}")

