package secao_13.metodosAbstratos.exerciciofixa.entities;

public class Individual extends TaxPayer {

    private Double healthExpenditures;

    public Individual(String name, Double anuallncome, double health) {
        super(name, anuallncome);
    }

    public Double getHealthExpenditures() {
        return healthExpenditures;
    }

    public void setHealthExpenditures(Double healthExpenditures) {
        this.healthExpenditures = healthExpenditures;
    }

    @Override
    public Double tax() {
        if (getAnualIncome() < 20000.0) {
            return getAnualIncome() * 0.15 - healthExpenditures * 0.5;
        }
        else {
            return getAnualIncome() * 0.25 - healthExpenditures * 0.5;
        }
    }

}
