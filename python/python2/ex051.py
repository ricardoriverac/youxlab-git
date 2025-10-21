primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao:'))
for c in range(primeirotermo, primeirotermo + 10 * razao, razao):
 print(f'Os dez primeiros termos dessa PA é {c}')