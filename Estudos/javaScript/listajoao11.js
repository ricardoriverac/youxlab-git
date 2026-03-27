const vetor = []

vetor.push("A","B","C","D", "E", "F")
const marcador = []
marcador.push("C", "F")

const inicio = vetor.indexOf(marcador[0])
const fim = vetor.indexOf(marcador[1])

const resultado = vetor.slice(inicio+1, fim)

console.log(resultado)