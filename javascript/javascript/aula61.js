const Pessoa={
    nome:"Bruno"
}

const p2=Pessoa
const p3=Pessoa

p3.nome="Cladisvardson"
p2["nome"]="Bridgertrudismelda"

console.log(Pessoa.nome);
console.log(p2.nome);
console.log(p3.nome);