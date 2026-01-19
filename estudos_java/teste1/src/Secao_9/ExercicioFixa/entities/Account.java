package Secao_9.ExercicioFixa.entities;


public class Account {
    private int accNumber;
    private String name;
    private double balance = 0;

    public Account(int accNumber, String name, double balance) {
        this.accNumber = accNumber;
        this.name = name;
        this.balance = balance;
    }

    public Account() {}

    public int getAccNumber() {
        return accNumber;
    }

    public void setAccNumber(int accNumber) {
        this.accNumber = accNumber;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double value) {
        this.balance += value;
    }

    public void withdraw(double value) {
        this.balance -= value + 5;
    }

    @Override
    public String toString() {
        return "Account " + accNumber +
                ", Holder: " + name +
                ", Balance: $ " + balance;
    }
}
