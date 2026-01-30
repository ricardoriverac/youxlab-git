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

// let valoresEletronicos = 0
// const produtosEletronicos = []
// for(const produto of produtos){
//     if(produto.categoria === 'Eletrônicos'){
//         valoresEletronicos += produto.estoque
//         produtosEletronicos.push(produto.nome)
//     }
// }

// let valoresPerifericos = 0
// const produtosPerifericos = []
// for(const produto of produtos){
//     if(produto.categoria === 'Periféricos'){
//         valoresPerifericos += produto.estoque
//         produtosPerifericos.push(produto.nome)
//     }
// }

// let valoresAcessorios = 0
// const produtosAcessorios = []
// for(const produto of produtos){
//     if(produto.categoria === 'Acessórios'){
//         valoresAcessorios += produto.estoque
//         produtosAcessorios.push(produto.nome)
//     }
// }

// let valoresArmazenamento = 0
// const produtosArmazenamento = []
// for(const produto of produtos){
//     if(produto.categoria === 'Armazenamento'){
//         valoresArmazenamento += produto.estoque
//         produtosArmazenamento.push(produto.nome)
//     }
// }

// let valoresMoveis = 0
// const produtosMoveis = []
// for(const produto of produtos){
//     if(produto.categoria === 'Móveis'){
//         valoresMoveis += produto.estoque
//         produtosMoveis.push(produto.nome)
//     }
// }

// let valoresRede = 0
// const produtosRedes = []
// for(const produto of produtos){
//     if(produto.categoria === 'Rede'){
//         valoresRede += produto.estoque
//         produtosRedes.push(produto.nome)
//     }
// }

// let valoresIluminacao = 0
// const produtosIluminacao = []
// for(const produto of produtos){
//     if(produto.categoria === 'Iluminação'){
//         valoresIluminacao += produto.estoque
//         produtosIluminacao.push(produto.nome)
//     }
// }

// let valoresUtilidades = 0
// const produtosUtilidades = []
// for(const produto of produtos){
//     if(produto.categoria === 'Utilidades'){
//         valoresUtilidades += produto.estoque
//         produtosUtilidades.push(produto.nome)
//     }
// }


// let valoresEnergia = 0
// const produtosEnergia = []
// for(const produto of produtos){
//     if(produto.categoria === 'Energia'){
//         valoresEnergia += produto.estoque
//         produtosEnergia.push(produto.nome)
//     }
// }

// console.log('Eletrônicos:',produtosEletronicos.toString(),[valoresEletronicos])
// console.log('Periféricos:',produtosPerifericos.toString(),[valoresPerifericos])
// console.log('Acessórios:',produtosAcessorios.toString(),[valoresAcessorios])
// console.log('Armazenamento:',produtosArmazenamento.toString(),[valoresArmazenamento])
// console.log('Móveis:',produtosMoveis.toString(),[valoresMoveis])
// console.log('Rede:',produtosRedes.toString(),[valoresRede])
// console.log('Iluminação:',produtosIluminacao.toString(),[valoresIluminacao])
// console.log('Utilidades:',produtosUtilidades.toString(),[valoresUtilidades])
// console.log('Energia:',produtosEnergia.toString(),[valoresEnergia])



const porCategoria = {};
//{'Eletrônicos': ['Notebook', 'Smartphone'], Periféricos: ['Mouse'] ......}

for (const produto of produtos){
    const categoria = produto.categoria;
    if (!porCategoria[categoria]){
        porCategoria[categoria]=[]
    }
    porCategoria[categoria].push(produto)
}
console.log(porCategoria);

for (const categoria in porCategoria){
    console.log(`Categoria: ${categoria}`);
    let totalEstoque = 0;
    for (const produto of porCategoria[categoria]){
        console.log(` -${produto.nome} | estoque ${produto.estoque}`);
        totalEstoque += produto.estoque
    }
    console.log(['Estoque total: ' + totalEstoque]);
}
