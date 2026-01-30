// const cursos=['HTML','CSS','Javascript','PHP','React']

// cursos.map((el,i)=>{
//     console.log('Curso:'+el+' ─ Sua posição no array:'+i)
// })

// let c=cursos.map((el,i)=>{
//     return el
// })
// console.log(c)

// let el=document.getElementsByTagName("div")
// el=[...el]
// el.map((e,i)=>{
//     e.innerHTML="CFB Cursos"
// })

// const el=document.getElementsByTagName("div")
// const val=array.prototype.map.call(el,({innerHTML})=>{innerHTMl})
// console.log(val)

const converterInt=(e)=>parseInt(e)
const dobrar=(e)=>e*2
let num=['1','2','3','4','5'].map(converterInt).map(dobrar)
console.log(num)