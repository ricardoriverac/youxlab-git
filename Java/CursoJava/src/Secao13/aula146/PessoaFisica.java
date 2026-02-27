package Secao13.aula146;

public class PessoaFisica extends ClasseAbs {
    private Double healthExpenditures;

    public PessoaFisica(String name, double renda, double healthExpenditures) {
        super(name, renda);
        this.healthExpenditures = healthExpenditures;
    }

    @Override
    public double tax() {
        double basicTax;

        if (getRenda() < 20000.0) {
            basicTax = getRenda() * 0.15;
        } else {
            basicTax = getRenda() * 0.25;
        }

        basicTax -= healthExpenditures * 0.5;

        return basicTax;
    }
}
