/* FOR IN , FOR OF */

const objs=document.getElementsByTagName("div")

let num = [10, 20, 30, 40, 50]

for(n of num){
    console.log(n)
}

console.log("=========================")


for(let i=0; i<num.length;i++){
    console.log(num[i])
}
