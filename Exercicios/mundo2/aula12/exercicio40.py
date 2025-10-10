nota1=int(input('Digite sua primeira nota: '))
nota2=int(input('Digite sua segunda nota: '))
nota_total= nota1 + nota2
media=nota_total/2

if media < 5.0:
    print("Você está reprovado!")
elif media>=5.0 and media <= 6.9:
    print("Voce está de recuperação!")
elif media>=7.0:
    print("Voce está aprovado!")