const vetor1 = [20,24,25,31,34,38,40,52,1,3]
const vetor2 = [2,15,3,4,7]

vetor1.map((vetor)=>{
    count = 0
    i=0
   for(let j = 0; j<vetor2.length - 1; j++){
    if(vetor%vetor2[j] == 0){
        count+=1
    }
   }
   console.log(vetor + " " + count)
})