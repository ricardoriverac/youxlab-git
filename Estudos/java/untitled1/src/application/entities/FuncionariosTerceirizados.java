package application.entities;

public class FuncionariosTerceirizados extends Funcionarios3{
    private Double salarioAdicional;
    public FuncionariosTerceirizados() {
        super();
    }

    public FuncionariosTerceirizados(String nomeFuncionario, Integer cargaHoraria, Double valorHora, Double salarioAdicional) {
        super(nomeFuncionario, cargaHoraria, valorHora);
        this.salarioAdicional = salarioAdicional;
    }

    public Double getSalarioAdicional() {
        return salarioAdicional;
    }

    public void setSalarioAdicional(Double salarioAdicional) {
        this.salarioAdicional = salarioAdicional;
    }

    @Override
    public  Double pagamento(){
        return super.pagamento() + salarioAdicional * 1.1;

    }
}
