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


const porCategoria = {};

// {Eletrônicos: ['Notebook', 'Smartphone'], Periféricos: ['MouseEvent', 'Teclado']}

for (const produto of produtos){
    const cat = produto.categoria
    if (!porCategoria[cat]){
        porCategoria[cat]=[]
    }    
    
    porCategoria[cat].push(produto);

}

// console.log(porCategoria);

for (const key in porCategoria) {    
    console.log(key + "----");
    const listaProdutosDaCategoria = porCategoria[key];
    // console.log(listaProdutosDaCategoria);
    for (const produtoAtual of listaProdutosDaCategoria) {
        console.log(produtoAtual.nome);
    }
}



let quantEletronicos = 0
let quantenergia = 0
let quantperifericos = 0
let quantacessorios = 0
let quantrede = 0
let quantutilidades = 0
let quantarmazenamento = 0
let quantmoveis = 0
let quantiluminacao = 0

produtos.map((el, i) => {
    if (el.categoria == "Eletrônicos") {
        quantEletronicos = quantEletronicos + el.estoque
    } else if (el.categoria == "Periféricos") {
        quantperifericos = quantperifericos + el.estoque
    } else if (el.categoria == "Acessórios") {
        quantacessorios = quantacessorios + el.estoque
    } else if (el.categoria == "Energia") {
        quantenergia = quantenergia + el.estoque
    } else if (el.categoria == "Rede") {
        quantrede = quantrede + el.estoque
    } else if (el.categoria == "Utilidades") {
        quantutilidades = quantutilidades + el.estoque
    } else if (el.categoria == "Armazenamento") {
        quantarmazenamento = quantarmazenamento + el.estoque
    } else if (el.categoria == "Móveis") {
        quantmoveis = quantmoveis + el.estoque
    } else if (el.categoria == "Iluminação") {
        quantiluminacao = quantiluminacao + el.estoque
    }
})

