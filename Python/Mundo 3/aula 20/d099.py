from time import sleep
def maior(* numero): #Isso está criando uma função chamada maior.
                    #*numero quer dizer que você pode colocar quantos números quiser dentro dela.
                    #Tipo: maior(1, 2, 3) ou maior(9, 4, 7, 0, 2, 5, 1)
    contador = maior = 0
    print('-- Analisando os valores digitados...')
    for valor in numero:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if contador == 0: #“Se é o primeiro número que estou vendo, então é o maior até agora.”
            maior = valor
        else:             #Depois, ele vai comparando todos os outros e pensando:
            if valor > maior:
                maior = valor   #“Esse novo número é maior do que o que eu achei antes? Se sim, atualiza!”
        contador += 1
    print(f'    Foram digitados {contador} números ao todo!')
    print(f'    O maior valor digitado foi {maior}.')


maior(2, 5, 1, 9, 0, 4)
maior(7, 3, 8, 2)
maior(1, 2, 3)
maior(7)
maior()
