comidas = [
    'pizza', 'hamburguer', 'lasanha', 'sushi', 'feijoada', 'churrasco', 'pastel', 'coxinha', 'empada', 'tapioca',
    'acaraje', 'pao de queijo', 'brigadeiro', 'esfiha', 'kibe', 'yakisoba', 'strogonoff', 'macarrao', 'batata frita', 'omelete',
    'panqueca', 'risoto', 'rabada', 'moqueca', 'farofa', 'feijao tropeiro', 'pao frances', 'salada', 'sanduiche', 'cachorro quente',
    'nhoque', 'canja', 'sopa de legumes', 'sopa de ervilha', 'carne assada', 'bife acebolado', 'frango assado', 'frango a passarinho', 'costela', 'picanha',
    'linguica', 'almondega', 'ensopado', 'camarao', 'lagosta', 'bacalhau', 'tilapia', 'peixe frito', 'caruru', 'vatapa',
    'maniçoba', 'caldo verde', 'tutu de feijao', 'dobradinha', 'galinhada', 'arroz carreteiro', 'virado a paulista', 'cuscuz', 'angu', 'polenta',
    'quibe cru', 'charuto', 'tabule', 'shawarma', 'falafel', 'escondidinho', 'pure de batata', 'panetone', 'churros', 'crepe',
    'waffle', 'torta de frango', 'torta de limao', 'torta de morango', 'bolo de cenoura', 'bolo de chocolate', 'pudim', 'mousse de maracuja', 'mousse de chocolate', 'sorvete',
    'milkshake', 'pipoca', 'doce de leite', 'goiabada', 'romeu e julieta', 'abacaxi', 'melancia', 'manga', 'banana frita', 'salada de frutas',
    'vatapá', 'acarajé', 'beiju', 'cuscuz nordestino', 'canjica', 'pamonha', 'curau', 'bolo de milho', 'bolo de fubá', 'bolo de mandioca'
]
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('ESCOLHA ALGUMA COMIDA DO CARDÁPIO')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
digite_a_sua_comida = str(input('Digite uma comida de sua preferência: ')).lower()

if digite_a_sua_comida in comidas:
    print(f'A comida "{digite_a_sua_comida}" está no cardápio.')
else:
    print(f'A comida "{digite_a_sua_comida}" não está no cardápio.')
