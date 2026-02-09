package secao13_Heranca.exercicioProposto2.entities;

public class PessoaJuridica extends TaxPayer {
    private int numberOfEmployees;

    public PessoaJuridica(String name, Double anualincome, int numberOfEmployees){
        super(name, anualincome);
        this.numberOfEmployees = numberOfEmployees;

    }

    public int getNumberOfEmployees(){
        return numberOfEmployees;
    }
    public void setNumberOfEmployees(int numberOfEmployees){
        this.numberOfEmployees = numberOfEmployees;
    }


    @Override
    public Double tax(){

        if (numberOfEmployees <= 10){
            return anualincome * (16.0/100.0);
        }
        else {
            return anualincome * (14.0/100.0);
        }
    }
}
