import random
computador=random.randint(1,2)
escolha_jogador = int(input("Qual a sua escolha \n [1] para impar \n [2] para par\n : "))
contador_vitorias = 0

while escolha_jogador == computador :
    contador_vitorias += 1
    print("Você acertou!")
    computador=random.randint(1,2)
    escolha_jogador = int(input("Qual a sua escolha \n [1] para impar \n [2] para par "))
            
print(f"Você perdeu! Mas teve o total de {contador_vitorias} de vitorias!")