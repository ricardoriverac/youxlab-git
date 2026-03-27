function intersecaoVetores(n1, n2, vetor1Str, vetor2Str) {
  const vetor1 = vetor1Str.split(" ").map(Number);
  const vetor2 = vetor2Str.split(" ").map(Number);
  const intersecao = [];

  for (let i = 0; i < vetor1.length; i++) {
    if (vetor2.includes(vetor1[i])) {
      intersecao.push(vetor1[i]);
    }
  }

  if (intersecao.length === 0) {
    return "-1";
  } else {
    return intersecao.join(" ");
  }
}

console.log(intersecaoVetores(5,3,"4 2 8 9 8 6", "2 5 0"))