palavras=('futebol','cristiano','messi','drogba','neymar','real madrid',
          'pep guardiola','dembele','vini jr')
for l in palavras:
    print(f'\nNa palavra {l} temos',end='')
    for let in palavras:
        if let.lower() in 'aeiou':
            print(let)