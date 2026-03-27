const v1 = "1 2 3 4 5".split(" ").map(Number);
let v2 = "10 35 11 2 1 0 0 0 0 0".split(" ").map(Number);

const posicao = 1;

let resultado = [];

for (let i = 0; i < v1.length; i++) {

  for (let j = v2.length - 1; j > posicao; j--) {
    v2[j] = v2[j - 1];
  }

  v2[posicao] = v1[i];

  resultado.push(v2.join(" "));
}

console.log(resultado.join("\n"));