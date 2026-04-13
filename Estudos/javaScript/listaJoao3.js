const vetor1 = [10,20,30,40,50,60,70]
const vetor2 = [0,6,3,1,-1]

 var multiplicacao
for(let i = 0; i<vetor2.length && vetor2[i] >=0; i++){
        
        if(i == 0)
            multiplicacao = vetor1[vetor2[i]]
        
        if(i > 0)
            multiplicacao *= vetor1[vetor2[i]]
}
console.log(multiplicacao)