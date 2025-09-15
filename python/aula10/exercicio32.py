#dizer se um ano é bissexto
ano = int(input('Digite o ano desejado: '))
print(f'o ano {ano} é bissexto' if ano % 4 == 0 else f'o ano {ano} não é bissexto')