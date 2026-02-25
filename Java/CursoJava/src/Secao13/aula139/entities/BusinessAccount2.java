package Secao13.aula139.entities;

public class BusinessAccount2 extends Account2 {
    private double loanLimit;

    public BusinessAccount2() {
        super();
    }

    public BusinessAccount2(Integer number, String holder, double balance, double loanLimit) {
        super(number, holder, balance);
        this.loanLimit = loanLimit;
    }

    public double getLoanLimit() {
        return loanLimit;
    }

    public void setLoanLimit(double loanLimit) {
        this.loanLimit = loanLimit;
    }

    public void loan(double amount) {
        if (amount <= loanLimit) {
            deposit(amount);
            balance += amount - 10.0;
        }
    }
    public void withdraw(double amount){
        super.withdraw(amount);
        balance -= 2.0;
    }
}