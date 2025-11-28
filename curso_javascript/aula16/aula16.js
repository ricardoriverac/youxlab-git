const objs=document.getElementsByClassName("div")

let num=[10,20,30,40,50]

for(let i=0; i<num.lenfth; i++){
    console.log(num[i]);
}

for(o in objs){
    console.log(o.innerHTML="Curso")
}

for(o in objs){
    console.log(objs[o].innerHTML)
}