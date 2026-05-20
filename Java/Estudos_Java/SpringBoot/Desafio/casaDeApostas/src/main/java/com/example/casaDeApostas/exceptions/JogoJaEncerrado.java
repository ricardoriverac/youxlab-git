package com.example.casaDeApostas.exceptions;

public class JogoJaEncerrado extends RuntimeException {
    public JogoJaEncerrado(String message) {
        super(message);
    }
}
