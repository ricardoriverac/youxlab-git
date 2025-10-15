def notas (a=0, b=0, c=0, sit=True):
    """notas (a=0, b=0, c=0, sit=True)
       -> Analisa notas com dicionarios
       :param a: recebe primeira nota
       : param b: recebe segunda nota
       : param c: recebe terceira nota
       : param sit=True: mostra que caso não haja verificação situação sempre será mostrada
       :return: com retorno"""
    info={}
    notes=[]
    notes.append(a)
    notes.append(b)
    notes.append(c)
    maior=0
    media=0
    menor=9999999
    for v in notes:
        if v > maior:
            maior=v
    for v in notes:
        if menor > v:
            menor=v
    media= sum(notes) / len(notes)
    info['MAIOR']= ':', maior
    info['TOTAL']= ':', len(notes)
    info['MENOR']= ':', menor
    info['MEDIA']= ':', media
    if media < 5:
        info['SITUACAO']= 'RUIM'
    if media > 5:
        info['SITUACAO']= 'BOA'
    exposição= str(input('Você deseja saber da sua situação?[S/N]').upper())
    if exposição != 'N':
        return (f'{info}')
    if exposição == 'N':
        info.pop("SITUACAO")
        return info






resp = notas(5.5, 2.5, 1.5)


print(resp)
