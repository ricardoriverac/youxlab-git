const caixa1=document.querySelector("#caixa1")
const btn_c=document.querySelector(".curso")
const c1_2=document.querySelector("#c1_2")
const cursos=["HTML","CSS","Javascript","PHP","React","MySQL","ReactNative"]

cursos.map((el,c)=>{
    const novoElemento=document.createElement("div")
    c+=1
    novoElemento.innerHTML=el
    novoElemento.setAttribute("id","c"+c)
    novoElemento.setAttribute("class","curso c1")
    
    const btn_lixeira=document.createElement("img")
    btn_lixeira.setAttribute("src","./img/lixeira.png")
    btn_lixeira.setAttribute("class","lixeira")
    btn_lixeira.addEventListener("click",(evt)=>{
        caixa1.removeChild(evt.target.parentNode)
    })

    novoElemento.appendChild(btn_lixeira)
    caixa1.appendChild(novoElemento)
})
