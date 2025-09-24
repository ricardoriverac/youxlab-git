primeiro = int(input('Digite o primeiro termo '))
razao = int(input('Digite a razão: '))
n = int(input('Quer q vá até qual termo? '))
ultimoTermo = primeiro + (n - 1) * razao
for c in range (primeiro, ultimoTermo, razao):
    print(c, end=' -> ')
print('fim')