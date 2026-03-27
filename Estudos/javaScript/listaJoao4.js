const vetor = [1,2,3,4,5,-5,-4,-1]
let vetorPositivo = []
let vetorNegativo = []
vetor.map((vetor) =>{
    if(vetor > 0 && vetorPositivo.length < 8){
        vetorPositivo.push(vetor)
    }
    if(vetor < 0 && vetorNegativo.length < 8){
        vetorNegativo.push(vetor)
    }
} )
console.log(vetorPositivo)
console.log(vetorNegativo)