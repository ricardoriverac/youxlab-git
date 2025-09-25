mp = 0                                                               #maior peso
mnp = 0                                                               #menor peso
for peso in range (1, 6):
    pp = float(input('|Digite qual o seu peso: '))                   #peso da pessoa
    if peso == 1 :
        mp = mp + pp
    if pp > mp:
        mp = mp + pp 
    if peso == 1:
        mnp = pp
    if pp < mnp :
        mnp = pp
print ('O maior peso é o de {}Kg e o menor peso é o de {}Kg' .format(mp, mnp))