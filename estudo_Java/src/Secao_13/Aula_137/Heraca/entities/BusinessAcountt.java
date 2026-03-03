package Secao_13.Aula_137.Heraca.entities;

public class BusinessAcountt extends Secao_13.Aula_137.Heraca.entities.Accountt {

    private Double loanLimit;

    public BusinessAcountt() {
        super();
    }

    public BusinessAcountt(Integer number, String holder, Double balance, Double loanLimit) {
        super(number, holder, balance);
        this.loanLimit = loanLimit;
    }

    public Double getLoanLimit() {
        return loanLimit;
    }

    public void setLoanLimit(Double loanLimit) {
        this.loanLimit = loanLimit;
    }

    public void loanLimit(double amount) {
        if (amount <= loanLimit)
            balance += amount - 10;
    }
}
