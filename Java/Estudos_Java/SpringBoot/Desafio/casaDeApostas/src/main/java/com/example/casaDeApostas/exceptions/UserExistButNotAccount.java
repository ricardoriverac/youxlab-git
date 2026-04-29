package com.example.casaDeApostas.exceptions;

public class UserExistButNotAccount extends RuntimeException {
    public UserExistButNotAccount(String message) {
        super(message);
    }
}
