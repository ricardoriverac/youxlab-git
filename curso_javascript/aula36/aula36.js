const caixa1=document.querySelector('#caixa1')
const caixa2=document.querySelector('#caixa2')
const btn_trasferir=document.querySelector('#btn_trasferir')
const todosCursos=[...document.querySelectorAll(".curso")]

todosCursos.map((el)=>{
    el.addEventListener('click',(evt)=>{
        const curso=evt.target
        curso.classList.toggle('selecionado')
    })
})

btn_trasferir.addEventListener("click",()=>{
    const cursosSelecionados=[...document.querySelectorAll(".selecionado")]
    const cursosNãoSelecionados=[...document.querySelectorAll(".curso:not(.selecionado)")]
    cursosSelecionados.map((el)=>{
            caixa2.appendChild(el)
    })   
    cursosNãoSelecionados.map((el)=>{
            caixa1.appendChild(el)
    })  
})