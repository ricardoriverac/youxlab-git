
// const cursos = ["HTML", "CSS", "JavaScript", "PHP", "REact"]
// cursos.map((elementos,indice)=>{
//     console.log("Cursos: " + elementos + " - Posição do curso: " +indice);
// })


/*
const cursos = ["HTML", "CSS", "JavaScript", "PHP", "REact"]
let c = cursos.map((el,i)=>{
   return el
})

console.log(c);
*/


// const cursos = ["HTML", "CSS", "JavaScript", "PHP", "REact"]
// let c = cursos.map((el,i)=>{
//    return "<div>"+el+"</div>"
// })
// console.log(c)


// let el = document.getElementsByTagName("div")
// el=[...el]
// console.log(el);
// el.map((e, i) => {
//     e.innerHTML = "CFB Cursos"
// })


// const el = document.getElementsByTagName("div")
// const val = Array.prototype.map.call(el,({innerHTML})=>{innerHTML})
// console.log(val)


const converterInt=(e)=>parseInt(e)
const dobrar =(e)=>(e)=>e*2
let num=["1", "2", "3", "4", "5"].map(dobrar)
console.log(num)