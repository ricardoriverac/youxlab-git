package secao_13.metodosAbstratos.exerciciofixa.entities;

public class Company extends TaxPayer {
    private Double numberOfEmployees;

    public Company(String name, Double anuallncome, int emp) {
        super(name, anuallncome);
    }

    public Double getNumberOfEmployees() {
        return numberOfEmployees;
    }

    public void setNumberOfEmployees(Double numberOfEmployees) {
        this.numberOfEmployees = numberOfEmployees;
    }

    @Override
    public Double tax() {
        if (numberOfEmployees > 10) {
            return getAnualIncome() * 0.14;
        }
        else {
            return getAnualIncome() * 0.16;
        }
    }
}
