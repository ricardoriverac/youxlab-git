const vetor = [4,6,3,9,7,10,13]
const multiplosde2 = vetor.filter(vetor => vetor % 2 === 0)
const multiplosde3 = vetor.filter(vetor => vetor % 3 === 0)
const multiplosJuncao = vetor.filter(vetor => vetor % 2 == 0 && vetor % 3 == 0)
if(multiplosde2.length === 0 && multiplosde3.length === 0){
    console.log(0)
}else{
    console.log(multiplosde2)
    console.log(multiplosde3)
    console.log(multiplosJuncao)
}