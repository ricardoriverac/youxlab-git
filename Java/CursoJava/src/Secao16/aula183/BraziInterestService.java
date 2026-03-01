package Secao16.aula183;

public class BraziInterestService {
    private double interestRate;

    public BraziInterestService(double interestRate) {
        this.interestRate = interestRate;
    }

    public double payment(double amount, int months) {
        return amount * Math.pow(1 + interestRate / 100, months);
    }
}
