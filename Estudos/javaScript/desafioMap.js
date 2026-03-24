const funcionarios = [
    {nome: 'José', salario: 1500, anosTrabalhados: 6},
    {nome: 'Maria', salario:2200, anosTrabalhados: 3},
    {nome: 'Everton', salario: 3000, anosTrabalhados: 5}
]
funcionarios.map((funcionario) =>{
    let newSalary = 0;
    if(funcionario.anosTrabalhados > 5){
        newSalary = funcionario.salario * 1.20
    }else{
        newSalary = funcionario.salario * 1.10
    }

    console.log(
        "Funcionário " + funcionario.nome + ": salario antigo = " + funcionario.salario.toFixed(2) + ", salario novo = " + newSalary.toFixed(2)
    )
    
 })
   