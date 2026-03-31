const funcionarios = [
    {nome: 'José', salario: 1500, anosTrabalhados: 6},
    { nome: 'Maria', salario: 2200, anosTrabalhados: 3 },
    { nome: 'Everton', salario: 3000, anosTrabalhados: 5 }
];

function calcularNovoSalario(funcionario) {
  if (funcionario.anosTrabalhados > 5) {
    return funcionario.salario * 1.2;
  } else {
    return funcionario.salario * 1.1;
  }
}

funcionarios.map(funcionario => {
  const novoSalario = calcularNovoSalario(funcionario);

  console.log('Funcionario: ' + funcionario.nome + ',Salario: ' + funcionario.salario + ',Novo Salario: ' + novoSalario)
});