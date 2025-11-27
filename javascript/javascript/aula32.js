const cursosTodos=[...document.getElementsByClassName("curso")]
const cursosC1=[...document.getElementsByClassName("curso")]
const cursosC2=[...document.getElementsByClassName("curso")]
const cursoEspecial=document.getElementsByClassName("curso")[6]

console.log(cursosTodos);
console.log(cursosC1);
console.log(cursosC2); 
console.log(cursoEspecial);

cursosC1.map((el)=>{
    el.classList.add("destaque")
})