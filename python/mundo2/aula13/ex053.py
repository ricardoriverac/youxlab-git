# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

def eh_palindromo(frase):
  frase_limpa = ' '.join(char for char in frase if char.isalnum()).lower()
  frase_invertida = frase_limpa[::-1]
  if frase_limpa == frase_invertida:
      if frase_limpa == frase_invertida:
          return True
  else:
   return False
frase_user = input('Digite uma frase para verificar se ela é palíndromo: ')
if eh_palindromo(frase_user):
    print(f'"{frase_user}" é um palíndromo!')
else:
    print(f'"{frase_user}" não é um palíndromo.')