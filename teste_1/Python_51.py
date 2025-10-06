print('==' * 20)
print('10 TERMOS DE UMA PA')
print('==' * 20)
primeirotermo = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = primeirotermo + (10 - 1) * razao
for c in range(primeirotermo,decimo + razao,razao):
    print('{}'.format(c), end='>')
print('ACABOU')


