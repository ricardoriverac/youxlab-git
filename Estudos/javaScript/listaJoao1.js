const vetorA = [5,6,7,8,9]
const vetorB = [5,4,3,2,1]
var soma = 0

    for(let i = vetorB.length - 1; i < 5; i++){
        soma+=vetorA[i] - vetorB[vetorB.length-1 - i]
    }

console.log(soma)