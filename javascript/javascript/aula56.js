const caixa=document.querySelector("#caixa")

const carros=["Polo","Golf","T-Cross","HRV"]

let ul=`<ul>`
carros.map((el)=>{
    ul+=`<li>${el}</<li>`
})
ul+ `</ol>`

caixa.innerHTML=ul