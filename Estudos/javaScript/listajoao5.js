const produtos = [1,2,3,4,5,6,7,8,9,10];
const estoques = [10,20,30,40,50,60,70,80,90,100]

const pedidos = [
    [1,2,10],
    [2,5,60],
    [3,20,5],
    [4,1,5],
    [0,0,0]
]

let naoAtendidosInexistente = 0
let naoAtendidoEstoque = 0

for(let pedido of pedidos){
    let cliente = pedido[0]
    let produto=pedido[1]
    let quantidade = pedido[2]

    if(cliente === 0)
        break

    let index = produtos.indexOf[produto]

    if(index === -1){
        naoAtendidosInexistente ++
    }
    else{
        if(estoques[index] >= quantidade){
            estoques[index] -= quantidade
        } else{
            naoAtendidoEstoque ++
        }
    }
}
for(let i = 0; i < produtos.length; i++){
    console.log(produtos[i]+ " " + estoques[i])
}

console.log(naoAtendidosInexistente)
console.log(naoAtendidoEstoque)