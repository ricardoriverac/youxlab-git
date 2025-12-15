const funcionarios = [
  { nome: 'José', salario: 1500, anosTrabalhados: 6 },
  { nome: 'Maria', salario: 2200, anosTrabalhados: 3 },
  { nome: 'Everton', salario: 3000, anosTrabalhados: 5 }
];

funcionarios.map(function (funcionario) {
  let novo_salario;

  if (funcionario.anosTrabalhados > 5) {
    novo_salario = funcionario.salario * 1.2;
  } else {
    novo_salario = funcionario.salario * 1.1;
  }

  console.log('Funcionário(a) ' + funcionario.nome +': salário antigo = ' + funcionario.salario +', salário novo = ' + novo_salario);
});
