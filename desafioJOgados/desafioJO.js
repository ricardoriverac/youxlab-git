const listaPoderesEL=document.getElementById("listaPoderes")
const btn_adicionar=document.getElementById("btn_Adicionar")
const poderInput=document.getElementById("poderInput")


let poderes=[]


btn_adicionar.addEventListener("click",(evt)=>{
    const valor = poderInput.value // pega o texto digitado
    if (valor !== "") {
        poderes.push(valor)
        poderInput.value = "" 
    }
    console.log(poderes);

    listaPoderesEL.innerHTML=""
    
    for(el of poderes){
        let li=document.createElement("li")
        li.textContent=el
        listaPoderesEL.appendChild(li)
    }
})

