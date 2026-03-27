function contarVogais(texto){
    let count = 0
    const vogais = "aeiouAEIOU"

    for(let letra of texto){
        if(vogais.includes(letra)){
            count ++
        }
    }
    return count
}
console.log(contarVogais("casa"))