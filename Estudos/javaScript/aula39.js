const caixa1= document.querySelector("#caixa1")
const btn_c=[...document.querySelectorAll(".curso")]
const c1_2=document.querySelector("#c1_2")
console.log(c1_2)
console.log(caixa1.hasChildNodes())

console.log(btn_c[0].hasChildNodes())
console.log(btn_c[0].childNodes)

if(caixa1.children.length > 0){
    console.log("A caixa tem filhos")
}else{
    console.log("A caixa não tem filhos")
}

console.log(caixa1.firstElementChild.innerHTML="TESTE")