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
]

let porCategoria = []

// for (let produto of produtos) {
//   let categoria = produto.categoria
//   porCategoria[categoria] = []
// }
// for (let produto of produtos) {
//     let categoria = produto.categoria
//     porCategoria[categoria]
// }
// if (!porCategoria[categoria]) { //essa linha pergunta c a categoria ainda não existe dentro do objeto (porCategoria) c n existir o if é executado,e c existir o if é ignorado
//     porCategoria[categoria] = 0 //essa linha so vai roda quando a categoria não existir
//   }



for (const categoria_atual in porCategoria) {
    console.log("Categoria: " + categoria_atual);
    console.log(porCategoria[categoria_atual])
}

let valoresRede = 0
let valoresEletronicos = 0
let valoresPerifericos = 0
let valoresAcessorios = 0
let valoresArmazenamento = 0
let valoresMoveis = 0
let valoresIluminação = 0
let valoresUtilidades = 0
let valoresEnergia = 0
const redes = []
const eletronicos = []
const perifericos = []
const acessorios = []
const armazenamento = []
const moveis = []
const iluminacao = []
const utilidades= []
const energia=[]

produtos.forEach(produto => {
    if (produto.categoria === 'Rede') {
        valoresRede += produto.estoque
        redes.push(produto.nome)

    }else if (produto.categoria === 'Eletrônicos') {
        valoresEletronicos += produto.estoque
        eletronicos.push(produto.nome)

    }else if (produto.categoria === 'Periféricos') {
        valoresPerifericos += produto.estoque
        perifericos.push(produto.nome)

    }else if (produto.categoria === 'Acessórios') {
        valoresAcessorios += produto.estoque
        acessorios.push(produto.nome)

    }else if (produto.categoria === 'Armazenamento') {
        valoresArmazenamento += produto.estoque
        armazenamento.push(produto.nome)

    }else if (produto.categoria === 'Móveis') {
        valoresMoveis += produto.estoque
        moveis.push(produto.nome)

    }else if (produto.categoria === 'Iluminação') {
        valoresIluminação += produto.estoque
        iluminacao.push(produto.nome)

    }else if (produto.categoria === 'Utilidades') {
        valoresUtilidades += produto.estoque
        utilidades.push(produto.nome)

    }else if (produto.categoria === 'Energia') {
        valoresEnergia += produto.estoque
        energia.push(produto.nome)
    }
})

console.log('Valore estoque Rede ' + valoresRede)
console.log('produtos da categoria rede: ' + redes.toString());

console.log('Valore estoque Eletronicos ' + valoresEletronicos)
console.log('produtos da categoria Eletronicos: ' + eletronicos.toString());

console.log('Valore estoque Perifericos ' + valoresPerifericos)
console.log('produtos da categoria Perifericos: ' + perifericos.toString());

console.log('Valore estoque Acessorios ' + valoresAcessorios)
console.log('produtos da categoria Eletronicos: ' + acessorios.toString());

console.log('Valore estoque Armazenamento ' + valoresArmazenamento)
console.log('produtos da categoria Armazenamento: ' + armazenamento.toString());

console.log('Valore estoque Moveis ' + valoresMoveis)
console.log('produtos da categoria Eletronicos: ' + moveis.toString());

console.log('Valore estoque Iluminação ' + valoresIluminação)
console.log('produtos da categoria Iluminação: ' + iluminacao.toString());

console.log('Valore estoque Utilidades ' + valoresUtilidades)
console.log('produtos da categoria Utilidades: ' + utilidades.toString());

console.log('Valore estoque Energia ' + valoresEnergia)
console.log('produtos da categoria Energia: ' + energia.toString());