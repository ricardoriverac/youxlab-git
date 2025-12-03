let n = 0
let max = 1000

while(n<max){
    console.log("Exercicio - " +n)
    if(n>10){
        break
    }
    n++
}

console.log("Fim do Programa")

console.log("======================")

let pares = 0 
for(let i=n;i<max;i++){
    console.log("Exercicio - " +i)
    if(i%2!=0){
        pares++
    }
}

console.log("Quantidade de pares: " + pares )
console.log("Fim do Programa")