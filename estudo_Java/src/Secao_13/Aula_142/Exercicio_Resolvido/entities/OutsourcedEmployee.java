package Secao_13.Aula_142.Exercicio_Resolvido.entities;

public class OutsourcedEmployee extends Employee{

    private Double additionalCharge;

    public OutsourcedEmployee() {
        super();
    }

    public OutsourcedEmployee(String name, Integer hours, Double valuePerHour, Double additional) {
        super(name, hours, valuePerHour);
        this.additionalCharge = additional;
    }

    public Double getAdditional() {
        return additionalCharge;
    }

    public void setAdditional(Double additional) {
        this.additionalCharge = additional;
    }

    @Override
    public double paymet() {
        return super.paymet() + additionalCharge * 1.1;
    }
}
