const funcionarios = [
    { nome: 'José', salario: 1500, anosTrabalhados: 6 },
    { nome: 'Maria', salario: 2200, anosTrabalhados: 3 },
    { nome: 'Everton', salario: 3000, anosTrabalhados: 5 }
];

let salarionovo

funcionarios.map((el, i) => {
    if (el.anosTrabalhados > 5) {
        salarionovo = el.salario * 1.2
        console.log("O funcionario " + el.nome + " recebia o salario de " + el.salario + ", mas seu novo salario será "+ salarionovo );
    }
    else {
        salarionovo = el.salario * 1.1
        console.log("O funcionario " + el.nome + " recebia o salario de " + el.salario + ", mas seu novo salario será "+ salarionovo.toFixed());
    }
})