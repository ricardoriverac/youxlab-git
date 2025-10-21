primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao:'))
termoatual = primeirotermo
termosgerados = 0 
while termosgerados < 10:
    print(termoatual)
    termoatual += razao
    termosgerados += 1 

