package Secao_13.Aula_142.Exercicio_Resolvido.entities;

public class OutsourcedEmployee extends Employee{

    private Double additional;

    public OutsourcedEmployee() {
        super();
    }

    public OutsourcedEmployee(String name, Integer hours, Double valuePerHour, Double additional) {
        super(name, hours, valuePerHour);
        this.additional = additional;
    }

    public Double getAdditional() {
        return additional;
    }

    public void setAdditional(Double additional) {
        this.additional = additional;
    }

    @Override
    public double payment() {
        return hours * valuePerHour ;
    }
}
