from random import choice
jogo = str(input('Vamos jogar jokenpô? '))
print("""Escolha:
      [1]PEDRA
      [2]PAPEL
      [3]TESOURA""")
opcao = int(input('Escolha uma opção: '))
opcao1 = str('PEDRA')
opcao2 = str('PAPEL')
opcao3 = str('TESOURA')
lista = [opcao1, opcao2, opcao3]
sorteado = choice(lista)
print(f'O computador escolheu {sorteado}')
ganhador = str(input('Quem ganhou? '))
