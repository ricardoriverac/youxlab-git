const temperatura = [31.5, 20.3, 30.4, 27.3, 22.1, 19.4, 15.3, 14.0, 19.9, 22.5, 29.3, 30.7]
const meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto","setembro", "outubro", "novembro", "dezembro"]
let maiorTemperatura = 0
let menorTemperatura = 999
let indiceMaior = 0;
let indiceMenor = 0
for(let i in temperatura){
        if(temperatura[i] > maiorTemperatura){
            maiorTemperatura = temperatura[i];
            indiceMaior = i;
        }

        if(temperatura[i] < menorTemperatura){
            menorTemperatura = temperatura[i]
            indiceMenor = i;
        }
}

console.log("Maior:", maiorTemperatura, "mês:", meses[indiceMaior])
console.log("Menor:", menorTemperatura, "-", meses[indiceMenor])