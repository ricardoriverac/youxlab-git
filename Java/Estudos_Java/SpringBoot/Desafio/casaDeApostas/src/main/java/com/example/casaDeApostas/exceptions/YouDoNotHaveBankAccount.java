package com.example.casaDeApostas.exceptions;

public class YouDoNotHaveBankAccount extends RuntimeException {
    public YouDoNotHaveBankAccount(String message) {
        super(message);
    }
}
