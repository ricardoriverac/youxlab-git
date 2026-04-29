package com.example.casaDeApostas.exceptions;

public class NaoPodeDepositarValorNegativo extends RuntimeException {
    public NaoPodeDepositarValorNegativo(String message) {
        super(message);
    }
}
