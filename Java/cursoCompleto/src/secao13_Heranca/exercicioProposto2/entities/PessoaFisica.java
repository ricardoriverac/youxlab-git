package secao13_Heranca.exercicioProposto2.entities;

public class PessoaFisica extends TaxPayer{
    private Double healthExpenditures;

    public PessoaFisica(String name, Double anualincome, Double healthExpenditures){
        super(name, anualincome);
        this.healthExpenditures = healthExpenditures;
    }
    public Double getHealthExpenditures(){
        return healthExpenditures;
    }
    public void setHealthExpenditures(double healthExpenditures){
        this.healthExpenditures = healthExpenditures;
    }

    @Override
    public Double tax(){
        double taxa = 0;
        if (anualincome <= 20000){
            taxa = (anualincome * 15/100) - (healthExpenditures * 50/100);
        }
        else {
            taxa = (anualincome * 25/100) - (healthExpenditures * 50/100);
        }
        return taxa;
    }
}