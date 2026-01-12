package secao_13.heranca.entitiesHeranca;

public class BusinessAccount extends Account{
    private Double loanLimit;

    public BusinessAccount(int number, String maria, double v, double loanLimit){

    }

    public BusinessAccount(Integer number, Double balence, String holder, Double loanLimit) {
        super(number, balence, holder);
        this.loanLimit = loanLimit;
    }


    public Double getLoanLimit() {
        return loanLimit;
    }



    public void setLoanLimit(Double loanLimit) {
        this.loanLimit = loanLimit;
    }



    public void loan(double amount){
        if (amount <= loanLimit){
            deposit(amount);
        }
    }
}


