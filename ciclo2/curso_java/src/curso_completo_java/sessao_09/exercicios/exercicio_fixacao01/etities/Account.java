package curso_completo_java.sessao_09.exercicios.exercicio_fixacao01.etities;

public class Account {

    private int numero;
    private String titular;
    private double balance;

    public Account(int numero, String titular) {
        this.numero = numero;
        this.titular = titular;
    }

    public Account(int numero, String titular, double deposito_inicial) {
        this.numero = numero;
        this.titular = titular;
        deposit(deposito_inicial);
    }

    public int getNumber() {
        return numero;
    }

    public String getHolder() {
        return titular;
    }

    public void setHolder(String titular) {
        this.titular = titular;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double quantia) {
        balance += quantia;
    }

    public void withdraw(double quantia) {
        balance -= quantia + 5.0;
    }

    public String toString() {
        return "Número da conta: "
                + numero
                + "\ntitular: "
                + titular
                + "\nsaldo: $ "
                + String.format("%.2f", balance);
    }
}





