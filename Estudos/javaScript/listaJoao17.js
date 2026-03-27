let palavra = []
const consoante = "bcdfghjklmnpqrstvwxyz"
let novaPalavra = []
palavra.push("brasileiro")

for(let letra of palavra[0]){
    if(consoante.includes(letra)){
        novaPalavra.push(letra)
    }
}
console.log(novaPalavra.join(""))