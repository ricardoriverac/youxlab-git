const btnJogar=document.getElementById("btnJogar")
const caixas1=[]
const caixas2=[]
const caixas3=[]

const caixa1=(el,c)=>{
    const novoElemento=document.createElement("div")
    c+=1
    novoElemento.innerHTML=el
    novoElemento.setAttribute("id",c)
    novoElemento.setAttribute("class","quadrado")
    linha1.appendChild(novoElemento)
}

const caixa2=(el,c)=>{
    const novoElemento=document.createElement("div")
    c+=1
    novoElemento.innerHTML=el
    novoElemento.setAttribute("id",c)
    novoElemento.setAttribute("class","quadrado")
    linha2.appendChild(novoElemento)
}

const caixa3=(el,c)=>{
    const novoElemento=document.createElement("div")
    c+=1
    novoElemento.innerHTML=el
    novoElemento.setAttribute("id",c)
    novoElemento.setAttribute("class","quadrado")
    linha3.appendChild(novoElemento)
}

btnJogar.addEventListener("click",(evt)=>{
    caixa1(caixas1,0)
    caixa1(caixas1,1)
    caixa1(caixas1,2)
    caixa2(caixas2,3)
    caixa2(caixas2,4)
    caixa2(caixas2,5)
    caixa3(caixas3,6)
    caixa3(caixas3,7)
    caixa3(caixas3,8)
    
})

const btnNJogar=document.getElementById("btnNJogar")

btnNJogar.addEventListener("cli9ck")


function removeevent(btnJogar){
    btnJogar.target.removeEventListener()
}