def maior(*numeros):
    maior_num = numeros[0]
    for n in numeros:
        if n > maior_num:
            maior_num = n
    print(f"o maior numero e {maior_num}")
maior(3,7,8,9)
maior(10,33,44,55) 
maior(87,34,99,77)           