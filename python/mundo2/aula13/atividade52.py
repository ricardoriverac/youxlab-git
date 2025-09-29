numero = int(input("digite um numero:"))
tot = 0 
for c in range(1,numero + 1):
    if numero % c == 0:
     print("\033[34m") 
     tot += 1
    else:
       print("\033[31m")
    print(f"{c}")   
print(f"O numero {numero} foi divisivel {tot} vezes")   
if tot ==2:
   print("ELE E PRIMO") 
else:
   print("NAO E PRIMO")   
   