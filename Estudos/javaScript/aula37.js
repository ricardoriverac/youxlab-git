const caixa1=document.querySelector("#caixa1")
const cursos = [...document.querySelectorAll(".curso")]

caixa1.addEventListener("click", (evt)=>{
    console.log("clicou")
    console.log(evt)
})

cursos.map((el)=>{
    
})
btn_c1.addEventListener("click", (evt)=>{
    evt.stopPropagation()
})