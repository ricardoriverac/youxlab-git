const funcionarios = [
    { nome: 'José', salario: 1500, anosTrabalhados: 6 },
    { nome: 'Maria', salario: 2200, anosTrabalhados: 3 },
    { nome: 'Everton', salario: 3000, anosTrabalhados: 5 }
];

funcionarios.map(funcionario => {
    let novoSalario;

    if (funcionario.anosTrabalhados > 5) {
        novoSalario = funcionario.salario * 1.2;
    } else {
        novoSalario = funcionario.salario * 1.1;
    }

    console.log(
        `Funcionário ${funcionario.nome}: salário antigo = ${funcionario.salario}, salário novo = ${novoSalario.toFixed()}`
    );
    return {
        ...funcionario,
        novoSalario
    };
});
