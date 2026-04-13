const funcionarios = [
    {nome: 'José', salario: 1500, anosTrabalhados: 6},
    {nome: 'Maria', salario:2200, anosTrabalhados: 3},
    {nome: 'Everton', salario: 3000, anosTrabalhados: 5}
];

funcionarios.forEach(funcionario => {
    const aumento = funcionario.anosTrabalhados > 5 ? 1.20 : 1.10;
    const newSalary = funcionario.salario * aumento;
    console.log(`Funcionário ${funcionario.nome}: salario antigo = ${funcionario.salario.toFixed(2)}, salario novo = ${newSalary.toFixed(2)}`);
});
