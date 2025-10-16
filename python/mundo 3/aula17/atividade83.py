parenteses = 0
palavra = str(input("digite uma expressao que use parenteses: " ))
for c in palavra:
    if c == "(":
        parenteses += 1 
    elif c == ")":
        parenteses -= 1
if parenteses == 0:
    print("todos parenteses foram fechados ")
elif parenteses < 0:
    print("tem parentes fechados a mais  ")
else:
    parenteses > 0
    print("tem parenteses abertos a mais")                  