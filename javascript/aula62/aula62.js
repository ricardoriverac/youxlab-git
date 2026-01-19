class Carro {  //classe pai
    constructor(nome, portas) {
        this.nome = nome
        this.portas = portas
        this.ligado = false
        this.vel = 0
        this.cor = ""
    }
    ligar = function () {
        this.ligado = true
    }
    desligar = function () {
        this.ligado = false
    }
}
setCor = function (cor) {
    this.cor = cor
}

class Militar extends Carro{ // Clsse filho 
    constructor(nome,portas,blindagem,municao){
        super(nome,portas)
        this.blindagem = blindagem
        this.municao = municao
    }
}

const c1 = new Carro ("Normal", 4)
c1.ligar()
c1.setCor("Preto")

console.log(`Nome: ${c1.nome}`);
console.log(`Portas: ${c1.portas}`);
console.log(`Ligado: ${c1.ligado}`);
console.log(`Velocidade: ${c1.vel}`);
console.log(`Cor: ${c1.cor}`);
console.log("-------------------------");

