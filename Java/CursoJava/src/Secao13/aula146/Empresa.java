package Secao13.aula146;

public class Empresa extends ClasseAbs {
    private Integer numberOfEmployees;

    public Empresa(String name, double renda, Integer numberOfEmployees) {
        super(name, renda);
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