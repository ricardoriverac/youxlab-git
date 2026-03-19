package Secao_14.Aula_154.Exercicio_Fixacao.entities;

import Secao_14.Aula_154.Exercicio_Fixacao.model_exception.SaldoInsuficienteException;

public class ContaBancaria {

    private Double saldo;

    public ContaBancaria(double saldo) throws IllegalArgumentException {
        if (saldo < 0) {
            throw new IllegalArgumentException("Erro: Saldo inicial não pode ser negativo!");
        }
        this.saldo = saldo;
    }

    public Double getSaldo() {
        return saldo;
    }

    public void sacar(double valor) throws SaldoInsuficienteException{
        if (valor > saldo) {
            throw new SaldoInsuficienteException("Erro: Saldo insuficiente para realizar o saque!");
        }
        this.saldo = this.saldo - valor;
    }

    @Override
    public String toString() {
        return "Saldo realizado com succeso!! " +
                "valor do saldo: " +
                saldo;
    }
}
