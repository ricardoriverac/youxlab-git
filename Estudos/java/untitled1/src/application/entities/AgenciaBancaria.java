package application.entities;

public class AgenciaBancaria {
    private int numConta;
    private String nome;
    private double depositoInicial;
    private double saldo;
    public AgenciaBancaria(int numConta, String nome, double depositoInicia){
        this.numConta = numConta;
        this.nome = nome;
        this.depositoInicial = depositoInicial;
    }
    public AgenciaBancaria(int numConta, String nome){
        this.numConta = numConta;
        this.nome = nome;
    }

    public void saldoInicial(double depositoInicial){
        saldo+= depositoInicial;
    }
    public void addSaldoo(double deposito){
        saldo += deposito;
    }
    public void removerSaldo(double saque){
        saldo -= saque;
    }
    public String toString(){
        return "Account " + getNumConta() + " Cliente: " + getNome() + "," + " Saldo: " + getSaldo();
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getSaldo() {
        return saldo;
    }

    public int getNumConta() {
        return numConta;
    }

}
