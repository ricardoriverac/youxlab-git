const v1 = "3 4 5 6 5 1 2 7 8 1 3".split(" ").map(Number);
const v2 = "6 1 2 3 4 5".split(" ").map(Number);

let sequencias = new Set();

for (let i = 0; i < v1.length; i++) {

  for (let j = i + 1; j < v1.length; j++) {

    let sub = v1.slice(i, j + 1);

    let consecutivo = true;

    for (let k = 0; k < sub.length - 1; k++) {
      if (sub[k] + 1 !== sub[k + 1]) {
        consecutivo = false;
        break;
      }
    }

    if (consecutivo) {
      let texto = sub.join(" ");

      if (v2.join(" ").includes(texto)) {
        sequencias.add(texto);
      }
    }
  }
}

if (sequencias.size === 0) {
  console.log("ERRO");
} else {
  console.log([...sequencias].join("\n"));
}