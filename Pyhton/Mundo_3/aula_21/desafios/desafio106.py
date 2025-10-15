def minissistema(funçao):
    return help(funçao)

while True:
    funcao = input("Qual função: ")
    if funcao == 'FIM':
        print("fim.")
        break
    
    minissistema(funcao)