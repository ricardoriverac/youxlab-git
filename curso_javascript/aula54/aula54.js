const caixa=document.querySelector("#caixa")

let mapa=new Map()

mapa.set("curso","Javascript")
mapa.set(10,"CFB Cursos")
mapa.set(1,100)
mapa.set("canal",100)

console.log(mapa);

if(mapa.has("canal")){
    caixa.innerHTML="A chave existe na coleção"
}else{
    caixa.innerHTML="A chave NÃO esta na coleção"
}
caixa.innerHTML=mapa.get("curso")