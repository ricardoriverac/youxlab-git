const n = 9;

let triangulo = [];

for (let i = 0; i < n; i++) {

  let linha = [];

  for (let j = 0; j <= i; j++) {

    if (j === 0 || j === i) {
      linha.push(1);
    } else {
      linha.push(triangulo[i - 1][j - 1] + triangulo[i - 1][j]);
    }

  }

  triangulo.push(linha);
}

console.log(triangulo.map(l => l.join(" ")).join("\n"));