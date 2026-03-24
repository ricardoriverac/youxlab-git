const dc1=document.getElementById
const dc2 = document.getElementById
const dc3=document.getElementById
const dc4 = document.getElementById
const dc5 = document.getElementById
const dc6 = document.getElementById

const arrayElementos = [dc1,dc2,dc3,dc4,dc5,dc6]

for(d of arrayElementos){
    d.innerHTML = "CFB cursos"
}

arrayElementos.map((e) =>{
    e.innerHTML="CFB cursos"
    console.log(e)
})
console.log(arrayElementos)