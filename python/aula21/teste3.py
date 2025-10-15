def teste():
    """
    escopo de variáveis
    parte do código onde estão armazenadas e localizadas uma variável
    existem formas de escopo, como escopo local, que delimita a funcionalidade de uma variável em um local(como é o caso de uma variável que foi definida dentro de uma função) e o escopo global, que permite a ampla funcionalidade da variável em todo o programa(como definir a variável dentro do programa principal) 
    OU seja, X é uma variável LOCAL e N é uma variável GLOBAL
    entretanto, caso uma variável global seja criada e uma outra variável local igual a global também seja criada, será dada preferência ao valo da variável local no escopo local dessa mesma variável
    a menos que, seja usado um comando chamado "global -variável-", ele define que seja usada a varável global, ao invés de criar uma nova dentro do escopo local
    isso permite alterar o valor de uma variável global já estabelecida dentro de uma função, por exemplo
    """
    x = 8
    print(f'O valor de "n" na função teste é {n}')
    print(f'O valor de "x" na função teste é de {x}')

n = 2
print(f'O valor de "n" no programa principal é {n}')
print('Não há como extrair o valor de "x" no programa principal, pois ele está no escopo local da função teste.')