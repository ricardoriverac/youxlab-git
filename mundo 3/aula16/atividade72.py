#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,de zero ate vinte 

#seu programa devera ler um numero pelo teclado (entre 0-20) e mostra-lo por extenso
numero = int(input("digite um numero entre 0-20: "))
numero_extenso =("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","desseseis","dessesete","dezoito","dezenove","vinte")
while numero < 0 and numero > 20:
    numero = int(input("digite um numero entre 0-20: "))
print(numero_extenso[numero] )    