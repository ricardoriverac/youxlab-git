/*
let n = 0

while(true){
    console.log(n)
    n++
}*/


//5! = 5*4*3*2*1 = 120

let n = 5
let fat = 1

while (n>=1){
    fat*= n
    //fat=fat*n
    n --
    n=n-1
}

console.log(fat);