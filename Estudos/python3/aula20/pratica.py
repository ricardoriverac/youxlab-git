# def contador(*num ):
#     for v in num:
#         print(f'{v}')
#     print(f'FIM')


# contador(2,1,2)
# contador(8,0)
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1

valores = [7, 2, 3, 4, 4, 6]
dobra(valores)
print(valores)