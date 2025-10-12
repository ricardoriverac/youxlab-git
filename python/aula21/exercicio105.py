def notas(*n, sit=False):
    boletim = {}
    nota = float(n)
    boletim['notas'] = nota
    maior = menor = count = media = valor = 0
    for c in range(0, notas):
        count += 1
        if count == 1:
            maior = menor = c
        else: 
            if c > maior: 
                maior = c
                boletim['maior'] = maior
            if c < menor:
                menor = c
                boletim['menor'] = menor
    while True:
        if boletim['media'] >= 5:
            print('TURMA APROVADA')
            sit = True
        else:
            print('TURMA REPROVADA')
        if sit:
            break
    print(boletim)
resp = notas(5, 2, 1, sit=True)
        