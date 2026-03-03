package Secao_13.Aula_138.Upcasting_e_downcasting.entities;

public class SavingsAccount extends Account{

    private Double interestRate;

    public SavingsAccount() {
        super();
    }

    public SavingsAccount(Integer number, String holder, Double balance, Double account) {
        super(number, holder, balance);
        interestRate = account;
    }

    public void updateBalance() {
        balance += balance * interestRate;
    }
}
