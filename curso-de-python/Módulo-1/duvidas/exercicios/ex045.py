import random
escolhaUsuario = str(input('Vamos jogar Jokenpô, faça sua escolha: ')).lower()
pedra = str('Pedra')
papel = str('Papel')
tesoura = str('Tesoura')
jokenpo = [pedra, papel, tesoura]
escolhaMaquina = random.choice(jokenpo)
print('Jo... ken... PÔ!!!')
if escolhaUsuario == escolhaMaquina:
    print(f'EMPATE!! Nós dois fezemos a mesma escolha! Você escolher {escolhaUsuario} e eu escolhi {escolhaMaquina}')