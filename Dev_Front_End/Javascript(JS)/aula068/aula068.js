class Carro {
  constructor(tipo, estagioTurbo) {
    this.turbo = new Turbo(estagioTurbo);
    if (tipo == 1) {
      this.velMax = 120;
      this.nome = "Normal";
    } else if (tipo == 2) {
      this.velMax = 160;
      this.nome = "Esportivo";
    } else if (tipo == 3) {
      this.velMax = 200;
      this.nome = "SuperCarro";
    }
    this.velMax += this.turbo;
  }
  info() {
    console.log(this.nome);
    console.log(this.velMax);
    console.log(this.turbo);
    console.log(
      "────────────────────────────────────────────────────────────────────────"
    );
  }
}

class Turbo {
  constructor(e) {
    if (e == 0) {
      this.pot = 0;
    }
    if (e == 1) {
      this.pot = 50;
    } else if (e == 2) {
      this.pot = 100;
    } else if (e == 3) {
      this.pot = 150;
    }
  }
}

class CarroEspecial extends Carro {
  constructor(estagioTurbo) {
    super(4, estagioTurbo);
    this.tipoInfo = 1;
    this.velMax = 300 + this.turbo.pot;
    this.nome = "Carro Especial";
  }
  info() {
    if (this.tipoInfo == 1) {
      super.info();
    } else {
      console.log(`Nome: ${this.nome}`);
      console.log(`V.Max: ${this.velMax}`);
      console.log(`Turbo: ${this.turbo.pot}`);
      console.log(
        "────────────────────────────────────────────────────────────────────────"
      );
    }
  }
}

const c1 = new Carro(1, 0);
const c2 = new Carro(1, 1);
const c3 = new CarroEspecial(3);

c1.info();
c2.info();
