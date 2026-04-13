const vetor1 = [20, 24, 25, 31, 34, 38, 40, 52, 1, 3, 30]
const vetor2 = [2, 15, 3, 4, 7]

for (let i = 0; i < vetor1.length; i++) {
  let count = 0

  for (let j = 0; j < vetor2.length; j++) {
    if (vetor1[i] % vetor2[j] === 0) {
      count++
    }
  }
  console.log(vetor1[i] + " " + count)
}
