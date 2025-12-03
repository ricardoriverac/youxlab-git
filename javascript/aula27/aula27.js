/* RETORNAR CORES 
function* cores(){
    yield "vermelho"
    yield "verde"
    yield "rosa"
}

const itc=cores()
console.log(itc.next().value)
console.log(itc.next().value)
console.log(itc.next().value)
*/

/*
function* perguntas(){
    const nome = yield "Qual seu nome?"
    const esporte = yield "Qual seu esporte favorito?"
    return "Seu nome é " + nome + ", seu esporte favorito é " + esporte 
}

const itp =  perguntas()
console.log(itp.next().value)
console.log(itp.next("Igor").value)
console.log(itp.next("Volêi").value)
*/

function* contador() {
    let i = 0
    while (true) {
        yield i++
        if (i>5)
            break

    }
}
const itc = contador()
for (let c of itc){
    console.log(c)
}

/*console.log(itc.next().value)
console.log(itc.next().value)*/