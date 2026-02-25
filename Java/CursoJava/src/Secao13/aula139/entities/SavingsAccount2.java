package Secao13.aula139.entities;

public class SavingsAccount2 extends Account2 {
    private double interestRate;

    public SavingsAccount2(){
        super();
    }
    public SavingsAccount2(Integer number, String holder, double balance, double interestRate) {
        super(number, holder, balance);
        this.interestRate = interestRate;
    }
    public double getInterestRate() {
        return interestRate;
    }
    public void setInterestRate(double interestRate) {
        this.interestRate = interestRate;
    }
    public void updateBalance() {
        balance += balance * interestRate;
    }
    @Override
    public void withdraw(double amount) {
        balance -= amount;
    }
}
