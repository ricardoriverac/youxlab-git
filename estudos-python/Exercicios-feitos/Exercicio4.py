#Analisa características do que eu escrever
algumaCoisa = input ('Digite algo: ')
print('O tipo primitivo desse valor é ', type(algumaCoisa))
print('Só possui espaços? ', algumaCoisa.isspace())
print('É um número? ' , algumaCoisa.isnumeric())
print('É uma palavra? ' , algumaCoisa.isalpha())
print('É letra e/ou número? ' , algumaCoisa.isalnum())
print('Só possui letra minúscula? ' , algumaCoisa.islower())
print('Só possui letra maiúscula? ' , algumaCoisa.isupper())