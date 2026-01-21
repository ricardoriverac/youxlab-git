class npc {
    constructor(energia) {
        this.energia = energia
        this.alerta = false
    }
    info = function () {
        console.log(`Energia: ${this.energia}`);
        console.log(`Energia: ${this.energia}`);

    }

}

const npc1 = new npc(100)
const npc2 = new npc(80)
const npc3 = new npc(30)

console.log(npc1.energia);
console.log(npc2.energia);
console.log(npc3.energia);