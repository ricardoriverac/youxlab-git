from datetime import date
actualYear = (date.today().year)
def voto(a):
    yourAge=actualYear-a
    if yourAge<16:
        print('Você não pode votar!')
    elif yourAge<18 or yourAge>=70:
        print('Seu voto é opcional!')
    elif 18<=yourAge<70:
        print('Você é obrigado a votar!')
yearOfBirth = int(input('Enter your year of birth:\n->'))
voto(yearOfBirth)