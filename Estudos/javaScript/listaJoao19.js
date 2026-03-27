let numeros = "324911285"
let remover = 5
let resultado = []
for(let digito of numeros){
    while(resultado.length > 0 && resultado[resultado.length - 1] < digito && remover > 0){
        resultado.pop();
        remover--
    }

    resultado.push(digito)
}

while(remover > 0){
    resultado.pop()
    remover--
}

console.log(resultado.join(""))