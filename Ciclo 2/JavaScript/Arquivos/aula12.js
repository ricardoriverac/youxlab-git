const objs = document.getElementsByTagName("div")

let n1=[10,20,30]
let n2= [11,22,33,44,55]
let n3= [...n1]

console.log("n1: " + n1)
console.log("n2: " + n2)
console.log("n3: " + n3)
console.log("tipo de n3: " + typeof(n3))


const soma= (n1,n2)=>{
    return n1+n2
}

let valores= [10,11]

console.log(soma(...valores))