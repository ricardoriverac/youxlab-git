import random

escolhaUsuario = str(input('Vamos jogar Jokenpô, faça sua escolha:\n\n \033[34m[1] Pedra  [2] Papel  [3] Tesoura \033[m\n\n')).lower()
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

jokenpo = [pedra, papel, tesoura]
escolhaMaquina = random.choice(jokenpo)
print('\033[33m\nJo... ken... PÔ!!!\033[m')

if escolhaUsuario == pedra and escolhaMaquina == tesoura or escolhaUsuario == papel and escolhaMaquina == pedra or escolhaUsuario == tesoura and escolhaMaquina == papel:
    print(f'PARABÉNS!!! Você venceu! Você escolheu \033[32m{escolhaUsuario}\033[m e eu escolhi \033[31m{escolhaMaquina}\033[m.')

elif escolhaMaquina == pedra and escolhaUsuario == tesoura or escolhaMaquina == papel and escolhaUsuario == pedra or escolhaMaquina == tesoura and escolhaUsuario == papel:
    print(f'X_x - Você perdeu! Você escolheu \033[32m{escolhaUsuario}\033[m e eu escolhi \033[31m{escolhaMaquina}\033[m.')

elif escolhaUsuario == escolhaMaquina:
    print(f'EMPATE!! Nós dois fezemos a mesma escolha! Você escolheu \033[32m{escolhaUsuario}\033[m e eu escolhi \033[31m{escolhaMaquina}\033[m.')