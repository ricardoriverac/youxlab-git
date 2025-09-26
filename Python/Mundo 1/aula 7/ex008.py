m = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a'.format(m))
# km = m*1000
# hm = m*100
# dam = m*10
# dm = m*0.1
cm = m*0.01
mm = m*0.001
print(f'{mm:.2f}mm\n {cm:.2f}cm\n')
# {dm:.2f}dam\n {dam:.2f}dm\n {hm:.2f}hm\n {km:.2f}km\n