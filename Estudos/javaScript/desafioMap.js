const funcionarios = [
    {nome: 'José', salario: 1500, anosTrabalhados: 6},
    {nome: 'Maria', salario:2200, anosTrabalhados: 3},
    {nome: 'Everton', salario: 3000, anosTrabalhados: 5}
]
funcionarios.map(f =>{
    let newSalary = 0;
    if(f.anosTrabalhados > 5){
        newSalary = f.salario * 1.20
    }else{
        newSalary = f.salario * 1.10
    }

    console.log(
        "Funcionário " + f.nome + ": salario antigo = " + f.salario + ", salario novo = " + newSalary
    )
    
 })
 
   