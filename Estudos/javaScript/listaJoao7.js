let vetor = []
const newElementos = [1,2,3,4,5]
for(elemento of newElementos){
    vetor.push(elemento);
    if(vetor.length > 10){
        vetor.pop()
    }
}

const p = 9
const posicao = 2
vetor.splice(2,0,p)

while(vetor.length < 10){
    vetor.push(0)
}
console.log(vetor)