'''sequencia de fibonacci -> 0 - 1 - 1 - 2 - 3 - 5 - 8 ...
escreva um programa que leia um número n e repita a quantidade n de termos de um sequencia de fibonacci'''
termoN = int(input('Digite a quantidade "n" de termos: '))
termo1 = 0 
termo2 = 2
count = 3
print(f'{termo1} - {termo2} ', end='')
'''como a repetição começará a partir do termo 3, o count começará após a terceira posição'''
while count <= termoN:
    termo3 = termo1 + termo2
    print(f'- {termo3} ', end = '')
    termo1 = termo2
    termo2 = termo3
    count += 1