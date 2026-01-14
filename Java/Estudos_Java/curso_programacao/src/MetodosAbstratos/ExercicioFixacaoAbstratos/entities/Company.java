package MetodosAbstratos.ExercicioFixacaoAbstratos.entities;

public class Company extends TaxPayer{

    private Integer numberOfEmployee;

    public Company(){
        super();
    }

    public Company(String name, Double anualIncome, Integer numberOfEmployee) {
        super(name, anualIncome);
        this.numberOfEmployee = numberOfEmployee;
    }

    public int getNumberOfEmployee() {
        return numberOfEmployee;
    }

    public void setNumberOfEmployee(int numberOfEmployee) {
        this.numberOfEmployee = numberOfEmployee;
    }

    @Override
    public Double tax(){
        if (numberOfEmployee > 10) {
            return getAnualIncome() * 0.14;
        }
        else {
            return getAnualIncome() * 0.16;
        }
    }
}
