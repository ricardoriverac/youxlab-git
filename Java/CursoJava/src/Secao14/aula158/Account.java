package Secao14.aula158;

public class Account {
    private Integer number;
    private String holder;
    private Double balance;
    private Double withdrawLimit;


    public Account(Integer number, String holder, Double balance, Double withdrawLimit) {
        this.number = number;
        this.holder = holder;
        this.balance = balance;
        this.withdrawLimit = withdrawLimit;
    }
    public void deposit(Double amount) {
        balance += amount;
    }
    public void withdraw(Double amount) {
        if (amount > balance) {
            System.out.println("Saque não permitido: Saldo insuficiente");
        } else if (amount > withdrawLimit) {
            System.out.println("Saque não permitido: Valor acima do limite de saque");
        } else {
            balance -= amount;
            System.out.println("Saque realizado com sucesso! Novo saldo: " + String.format("%.2f", balance));
        }
}
}
