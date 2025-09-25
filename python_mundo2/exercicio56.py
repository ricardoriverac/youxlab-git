pdm = 0                                          #pessoas de maior
pmd = 0                                          #pessoas menor de idade
for vp in range (1, 8):
    p = int(input('Em qual ano você nasceu? '))                      #pergunta
    if p > 2007 :
        pdm = pdm + 1
    if p <= 2007 :
        pmd = pmd + 1
print ('{} pessoas são maior de idade e {} são menores de idade' .format(pdm, pmd))