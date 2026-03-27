const numeros = [1,2,2,3,3,4,4,4]

let maisRepetido = []
let maiorContagem = 0

for(let i = 0; i < numeros.length; i++){
    let contagem = 0

    for(let j = 0; j < numeros.length; j++){
        if(numeros[i] === numeros[j])
            contagem++
    }


if(contagem > maiorContagem){
    maiorContagem = contagem
    maisRepetido = numeros[i]
}
}
console.log(maisRepetido)