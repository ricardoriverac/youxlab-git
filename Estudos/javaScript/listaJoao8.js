const vetor = []

vetor.push(13,49,23,6,21)

let numeroRemovido = 13

if(vetor.includes(13)){
    let index = vetor.indexOf(13)
    vetor.splice(index, 1)
}else{
    console.log("Elemento não encontrado")
}

console.log(vetor)