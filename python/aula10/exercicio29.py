
sf = float(input('Digite um valor: '))
si = float(input('Digite um valor(2): '))
t = float(input('Digite um valor(3): '))
vm = (sf - si)/t
if vm > 80:
    multa = float(vm*7)
    print(f'Tomou multa \nSão R${multa} \nVc correu {vm}Km/h')
else:
    print('tranquilo')