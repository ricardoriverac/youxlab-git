const objs1=document.getElementsByTagName("div")
const objs2=[...document.getElementsByTagName("div")]

/*
const soma=(v1,v2,v3)=>{
    return v1+v2+v3
}
let valores=[1,5,4,10]
console.log(soma(...valores))
*/

objs2.forEach(element=>{
    element.innerHTML="curso"
});

console.log(objs1)
console.log(objs2)