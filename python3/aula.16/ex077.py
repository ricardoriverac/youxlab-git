minhaTupla = ('aprender', 'programar','linguagem','python','curso','lab',
'estudar','praticar','trabalhar','mercado','programador','futuro')
vogais = 'aeiou'
for palavra in minhaTupla:
    print(f'vogais da palavra {palavra.upper()} sao:', end= '')
    for vogal in vogais:
        if vogal in palavra.lower():
            print(f'{vogal} ',end='')
    print()        

    
    