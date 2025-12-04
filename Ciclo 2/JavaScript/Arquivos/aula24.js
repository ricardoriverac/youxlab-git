/* Funções Anônimas */ 
/*
let f=function(v1, v2){
    return v1 + v2
}
*/

//console.log(f(10, 5))

const f=new Function("n1", "n2", "n3", "return n1 + n2 + n3")

console.log(f(10,5,15))