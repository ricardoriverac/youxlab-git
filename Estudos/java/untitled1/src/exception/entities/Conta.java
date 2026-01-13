package exception.entities;

import exception.exception.InsufficientBalanceException;
import exception.exception.WithdrawalLimitExceededException;

public class Conta {
    private Integer numero;
    private String titular;
    private Double saldo;
    private Double limiteSaque;

    public Conta(Integer numero, String titular, Double saldo, Double limiteSaque) {
        this.numero = numero;
        this.titular = titular;
        this.saldo = saldo;
        this.limiteSaque = limiteSaque;
    }

    public Integer getNumero() {
        return numero;
    }


    public String getTitular() {
        return titular;
    }

    public void setTitular(String titular) {
        this.titular = titular;
    }

    public Double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public Double getLimiteSaque() {
        return limiteSaque;
    }

    public void setLimiteSaque(Double limiteSaque) {
        this.limiteSaque = limiteSaque;
    }

    public void deposito(Double quantidade){
        saldo+= quantidade;
    }

    public void saque(Double quantidade){
        if(quantidade > saldo && quantidade < limiteSaque){
            throw new InsufficientBalanceException("Caro usuário, você não possui saldo suficiente!");
        }
        if(limiteSaque < quantidade){
            throw  new WithdrawalLimitExceededException("Caro usuário, não é possível sacar um valor maior que seu limte");
        }
        else {
            saldo -= quantidade;
        }
    }

    @Override
    public String toString() {
        return "Novo saldo: " + saldo;
    }
}
