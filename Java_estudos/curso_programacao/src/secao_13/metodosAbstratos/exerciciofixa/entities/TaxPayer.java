package secao_13.metodosAbstratos.exerciciofixa.entities;

public abstract class TaxPayer {
    private String name;
    private Double AnualIncome;


    public TaxPayer(String name, Double anuallncome) {
        this.name = name;
        this.AnualIncome = anuallncome;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getAnualIncome() {
        return AnualIncome;
    }

    public void setAnualIncome(Double anualIncome) {
        this.AnualIncome = anualIncome;
    }

    public abstract Double tax();
}
