const caixa1=document.querySelector("#caixa1")
const btn_c=document.querySelector(".curso")
const c1_2=document.querySelector("#c1_2")
const cursos=["HTML","CSS","Javascropt","PHP","React","MySQL","ReactNative"]

cursos.map((el,c)=>{
    const novoElemento=document.createElement("div")
    c+=1
    novoElemento.innerHTML=el
    novoElemento.setAttribute("id","c"+c)
    novoElemento.setAttribute("class","curso c1")
    caixa1.appendChild(novoElemento)
})
