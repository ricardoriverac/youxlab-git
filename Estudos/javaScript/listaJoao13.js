const vetor = []
let maiorElemento = -Infinity;
let indexMaiorElemento = 0
let menorElemento = Infinity
let indexMenorElemento = 0
let elementoCentral = 0;
let indexElementoCentral = 0;
vetor.push(5,3,1,6,9,7)
for(let i in vetor){
    if(vetor[i] > maiorElemento){
        maiorElemento = vetor[i]
    }
    if(vetor[i] < menorElemento){
        menorElemento = vetor[i]
    }
}
if(vetor.length%2 !== 0){
        elementoCentral = vetor[Math.floor(vetor.length / 2)]
        indexElementoCentral = Math.floor(vetor.length/2)
    }else{
        elementoCentral = -1
        indexElementoCentral = -1
    }

console.log(maiorElemento)
console.log(menorElemento)
console.log(elementoCentral)
console.log(indexMaiorElemento)
console.log(indexMenorElemento)
console.log(indexElementoCentral)