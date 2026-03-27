const vetor = [9.4, 2.5, 1, 5.9, 1.6, -1, -6.7, -8.1, -2.3, -9.5]
let countNegativo = 0;
let somaPositivo = 0;
for(let elemento of vetor){
    if(elemento >= 0){
        somaPositivo+=elemento
    }else{
        countNegativo++
    }
}
console.log(countNegativo)
console.log(somaPositivo.toFixed(2))