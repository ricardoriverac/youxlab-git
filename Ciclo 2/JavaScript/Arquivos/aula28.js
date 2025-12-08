/* método MAP */

const cursos=['HTML', 'CSS', 'Javascript', 'PHP', 'React']
cursos.map((el, i)=> {
    console.log("Curso" + el + " - Posição do Curso " + i)
})  

console.log("-------------------------------------------------")

const cursos2=['HTML', 'CSS', 'Javascript', 'PHP', 'React']
let c=cursos2.map((el, i)=> {
    return el
})  

console.log(c)

console.log("-------------------------------------------------")

const el=document.getElementsByName("div")
el=[...el]
el.map((e,i)=>{
    console.log(e.innerHTML)
})
