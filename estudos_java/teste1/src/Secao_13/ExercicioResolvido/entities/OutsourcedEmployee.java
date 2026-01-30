package Secao_13.ExercicioResolvido.entities;

public class OutsourcedEmployee extends Employee{

    Double addicitionalCharge;

    public OutsourcedEmployee() {
    }

    public OutsourcedEmployee(String name, Integer hours, Double valuePerHour, Double addicitionalCharge) {
        super(name, hours, valuePerHour);
        this.addicitionalCharge = addicitionalCharge;
    }

    public Double getAddicitionalCharge() {
        return addicitionalCharge;
    }

    public void setAddicitionalCharge(Double addicitionalCharge) {
        this.addicitionalCharge = addicitionalCharge;
    }

    @Override
    public double payment() {
        return super.payment() + addicitionalCharge * 1.1;
    }
}
