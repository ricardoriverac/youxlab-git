const caixa=document.querySelector("#caixa")

let dados=["azul","verde","vermelho"]
let cursos=["html","css","JavaScript",cores]

//cursos[0]=2023

//cursos.push("c++")
// cursos.unshift("pyton")
// cursos.shift()

console.log(cursos[3][3][2]);

cursos.map((el)=>{
    let p=document.createElement("p")
    p.innerHTML=el
    caixa.appendChild(p)
})