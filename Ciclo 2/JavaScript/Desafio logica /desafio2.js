const produtos = [ 
{ nome: "Notebook", categoria: "Eletrônicos", preco: 3500, estoque: 5 }, 
{ nome: "Mouse", categoria: "Periféricos", preco: 80, estoque: 25 }, 
{ nome: "Teclado Mecânico", categoria: "Periféricos", preco: 250, estoque: 12 }, 
{ nome: "Smartphone", categoria: "Eletrônicos", preco: 2200, estoque: 8 }, 
{ nome: "Monitor", categoria: "Eletrônicos", preco: 900, estoque: 10 }, 
{ nome: "Pen Drive 32GB", categoria: "Acessórios", preco: 45, estoque: 50 }, 
{ nome: "HD Externo", categoria: "Armazenamento", preco: 400, estoque: 7 }, 
{ nome: "Webcam", categoria: "Periféricos", preco: 320, estoque: 15 }, 
{ nome: "Impressora", categoria: "Periféricos", preco: 850, estoque: 4 },
{ nome: "Cadeira Gamer", categoria: "Móveis", preco: 1500, estoque: 3 }, 
{ nome: "Roteador", categoria: "Rede", preco: 300, estoque: 9 }, 
{ nome: "Headset", categoria: "Acessórios", preco: 200, estoque: 20 }, 
{ nome: "Tablet", categoria: "Eletrônicos", preco: 1800, estoque: 6 }, 
{ nome: "Carregador Portátil", categoria: "Acessórios", preco: 120, estoque: 30 }, 
{ nome: "Cabo HDMI", categoria: "Acessórios", preco: 60, estoque: 40 }, 
{ nome: "Switch de Rede", categoria: "Rede", preco: 250, estoque: 11 }, 
{ nome: "Luminária LED", categoria: "Iluminação", preco: 100, estoque: 18 }, 
{ nome: "Extensão Elétrica", categoria: "Utilidades", preco: 70, estoque: 35 }, 
{ nome: "Notebook Gamer", categoria: "Eletrônicos", preco: 7500, estoque: 2 }, 
{ nome: "Estabilizador", categoria: "Energia", preco: 350, estoque: 5 } 
];

let redeEstoque = 0
let energiaEstoque = 0
let iluminacaoEstoque = 0
let eletronicosEstoque = 0
let perifericosEstoque = 0
let acessoriosEstoque = 0
let armazenamentoEstoque = 0
let moveisEstoque = 0 
let utilidadesEstoque = 0 


const produtosRede = []
const produtosEnergia = []
const produtosIluminacao = []
const produtosEletronicos = []
const produtosPerifericos = []
const produtosAcessorios = []
const produtosArmazenamento = []
const produtosMoveis = []
const produtosUtilidades = []

produtos.forEach(produto => {
    if (produto.categoria === 'Rede') {
        redeEstoque += produto.estoque
        produtosRede.push(produto.nome)
    } else if (produto.categoria === 'Energia'){
        energiaEstoque += produto.estoque
        produtosEnergia.push(produto.nome)
    } else if (produto.categoria === 'Iluminação'){
        iluminacaoEstoque += produto.estoque
        produtosIluminacao.push(produto.nome)
    }else if (produto.categoria === 'Eletrônicos'){
        eletronicosEstoque += produto.estoque
        produtosEletronicos.push(produto.nome)
    }else if (produto.categoria === 'Periféricos'){
        perifericosEstoque += produto.estoque
        produtosPerifericos.push(produto.nome)
    }else if (produto.categoria === 'Acessórios'){
        acessoriosEstoque += produto.estoque
        produtosAcessorios.push(produto.nome)
    }else if (produto.categoria === 'Armazenamento'){
        armazenamentoEstoque += produto.estoque
        produtosArmazenamento.push(produto.nome)
    }else if (produto.categoria === 'Móveis'){
        moveisEstoque += produto.estoque
        produtosMoveis.push(produto.nome)
    }else if (produto.categoria === 'Utilidades'){
        utilidadesEstoque += produto.estoque
        produtosUtilidades.push(produto.nome)}
    })

console.log('------------------------------------------------------------------------------');
console.log('Categoria Rede: ' + produtosRede);
console.log('Quantidade produtos rede: ' + redeEstoque );
console.log( );
console.log('Categoria Energia: ' + produtosEnergia);
console.log('Quantidade produtos energia: ' + energiaEstoque);
console.log( );
console.log('Categoria Iluminação: ' + produtosIluminacao);
console.log('Quantidade produtos Iluminação: ' + iluminacaoEstoque);
console.log( );
console.log('Categoria Eletrônicos: ' + produtosEletronicos);
console.log('Quantidade produtos eletrônicos: ' + eletronicosEstoque);
console.log( );
console.log('Categoria Perifericos: ' + produtosPerifericos);
console.log('Quantidade produtos perifericos: ' + perifericosEstoque);
console.log( );
console.log('Categoria Acessorios: ' + produtosAcessorios);
console.log('Quantidade produtos acessorios: ' + acessoriosEstoque);
console.log( );
console.log('Categoria Armazenamento: ' + produtosArmazenamento);
console.log('Quantidade produtos Armazenamento: ' + armazenamentoEstoque);
console.log( );
console.log('Categoria Moveis: ' + produtosMoveis);
console.log('Quantidade produtos moveis: ' + moveisEstoque);
console.log( )
console.log('Categoria Utilidades: ' + produtosUtilidades);
console.log('Quantidade produtos utilidades: ' + utilidadesEstoque);
console.log('------------------------------------------------------------------------------');