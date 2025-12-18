let funcionarios=[
    { nome: 'José', salario: 1500, anosTrabalhados: 6 },
    { nome: 'Maria', salario: 2200, anosTrabalhados: 3 },
    { nome: 'Everton', salario: 3000, anosTrabalhados: 5 }
]

let numero;

funcionarios.map((el,ind)=>{
    
      if(el.anosTrabalhados<=5){
         numero=el.salario*1.1
        console.log("Funcionario: " + el.nome, "Salario aumentado: " + numero);
    }else{
         numero=el.salario*1.2
         console.log("Funcionario: " + el.nome, "Salario aumentado: " + numero);
        }
    })
