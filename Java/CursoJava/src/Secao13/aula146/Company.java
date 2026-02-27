package Secao13.aula146;

public class Company extends ClasseAbs{
    private Integer numberOfEmployees;

    public Company(String name, Double annualIncome, Integer numberOfEmployees) {
        super(name, annualIncome);
        this.numberOfEmployees = numberOfEmployees;
    }

    @Override
    public double tax() {

        if (numberOfEmployees > 10) {
            return getRenda() * 0.14;
        } else {
            return getRenda() * 0.16;
        }
    }
}
