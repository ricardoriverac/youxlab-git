anodn = int(input('Qual ano você nasceu? '))                                           #ano de nascimento
idade = 2025 - anodn 
if idade < 9 :
    print ('mirin, {} de idade' .format(idade))
elif idade >9 and idade < 14 :
    print ('infantil, {} de idade' .format(idade))
elif idade > 14 and idade < 19:
    print ('junior, {} de idade'.format(idade))
elif idade > 19 and idade < 25:
    print ('sênior, {} de idade' .format(idade))
else:
    idade > 25
    print ('master,{} de idade' .format(idade))