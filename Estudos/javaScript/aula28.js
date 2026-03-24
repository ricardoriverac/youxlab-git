//const cursos = ['HTML', 'CSS', 'Javascript', 'PHP', 'React']
//cursos.map((e1, i)=>{
//    console.log("Curso: " + e1 + " - Posição do curso: " + i)
//let el=document.getElementsByTagName("div")
//el=[...el]
//el.map((e,i)=>{
//    console.log(e.innerHTML)
//})

//const el = document.getElementsByTagName("div")
//const val=Array.prototype.map.call(el,({innerHTML})=>innerHTML)
//console.log(val)

const converterInt=(e)=>parseInt(e)
const dobrar = (e)=>e*2
let num=['1','2','3','4','5'].map(dobrar)

console.log(num)