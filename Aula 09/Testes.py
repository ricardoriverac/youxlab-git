# fatiar a frase
frase = 'Curso em Vídeo Python'
print(frase [3:13] )

print(frase [:13])

print(frase [13:])

print(frase [1:15:2])

print(frase[1::2])

print(frase [::2])


print(frase.count('o'))

print(frase.upper().count('O'))

print(len(frase))

print(len(frase.strip()))

print(frase.replace('Python', 'Android'))

frase = (frase.replace('Python', 'Android'))
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))
print(frase.split())