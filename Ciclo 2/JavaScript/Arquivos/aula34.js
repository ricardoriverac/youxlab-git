// const c1 = document.getElementById("c1")
const cursos=[...document.querySelectorAll(".curso")]

// const msg=()=>{
//     alert("clicou")
// }

cursos.map((el)=>{
    el.addEventListener("click", (evt)=>{
    const el=evt.target
    el.classList.add("destaque")
    console.log(el.id + " foi clicado")
    })
})



// c1.addEventListener("click", (evt)=>{
//     const el=evt.target
//     el.classList.add("destaque")
// })
