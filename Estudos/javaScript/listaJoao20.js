let numero = 4;

let vistos = new Set();
let atual = numero;
let sequencia = [];

while (atual !== 1 && !vistos.has(atual)) {
  vistos.add(atual);
  sequencia.push(atual);

  let soma = 0;

  let texto = atual.toString();

  for (let digito of texto) {
    soma += digito * digito;
  }

  atual = soma;
}

sequencia.push(atual);

sequencia.shift();

console.log(sequencia.join(" "));

if (atual === 1) {
  console.log("sim");
} else {
  console.log("nao");
}