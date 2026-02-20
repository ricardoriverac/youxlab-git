package Secao9.Aula89.utiliz;

public class conta {
    private int number;
    private String holder;
    private double balance;

    public conta() {
    }
    public conta(int number, String holder, double valorinicial) {
        this.number = number;
        this.holder = holder;
        deposito(valorinicial);
    }
    public conta(int number, String holder) {
        this.number = number;
        this.holder = holder;
    }
    public int getNumber() {
        return number;
    }
    public String getHolder() {
        return holder;
    }
    public void setHolder(String holder) {
        this.holder = holder;
    }
    public double getBalance() {
        return balance;
    }
    public void deposito(double quantidade) {
        balance += quantidade;
    }
    public void saque(double quantidade) {
        balance -= quantidade + 5.0;
    }
    public String toString(){
        return "Account "
                +number
                +", holder: "
                +holder
                +", balance: $"
                +String.format("%.2f", balance);
    }
}
