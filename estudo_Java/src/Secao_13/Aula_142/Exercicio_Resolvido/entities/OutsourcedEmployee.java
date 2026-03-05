package Secao_13.Aula_142.Exercicio_Resolvido.entities;

public class OutsourcedEmployee extends Employee{

    private Double additinalCharg;

    public OutsourcedEmployee() {
        super();
    }

    public OutsourcedEmployee(Double additinalCharg) {
        this.additinalCharg = additinalCharg;
    }

    public OutsourcedEmployee(String name, Integer hours, Double valuePerHour, Double additinalCharg) {
        super(name, hours, valuePerHour);
        this.additinalCharg = additinalCharg;
    }

    public Double getAdditinalCharg() {
        return additinalCharg;
    }

    public void setAdditinalCharg(Double additinalCharg) {
        this.additinalCharg = additinalCharg;
    }
}
