package secao_13.heranca.entitiesHeranca;

public class SavingsAccount  extends Account{
    private Double interstRate;


    public SavingsAccount(int number, String anna, double v, double interstRate){
        super();
    }



    public SavingsAccount(Integer number, Double balence, String holder, Double interstRate) {
        super(number, balence, holder);
        this.interstRate = interstRate;
    }


    public Double getInterstRate() {
        return interstRate;
    }


    public void setInterstRate(Double interstRate) {
        this.interstRate = interstRate;
    }


    public void updateBalance(){
        balance= balance * interstRate;
    }
}
