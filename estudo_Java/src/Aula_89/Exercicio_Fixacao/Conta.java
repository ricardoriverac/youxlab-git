package Aula_89.Exercicio_Fixacao;

public class Conta {

    private final int numero = 2010;
    private String titular;
    private double saldo = 0;

    //Saldo
    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    //Titular
    public String getTitular() {
        return titular;
    }

    public void setTitular(String titular) {
        this.titular = titular;
    }

    //Numero
    public int getNumero() {
        return numero;
    }

    //Função
    public void deposito(double valor){
        this.saldo += valor;
    }

    public void saque(double valor){
        valor += 5;
        this.saldo -= valor;
    }

}
