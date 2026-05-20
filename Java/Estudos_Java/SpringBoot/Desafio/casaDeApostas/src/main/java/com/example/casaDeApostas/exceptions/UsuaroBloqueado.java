package com.example.casaDeApostas.exceptions;

public class UsuaroBloqueado extends RuntimeException {
    public UsuaroBloqueado(String message) {
        super(message);
    }
}
