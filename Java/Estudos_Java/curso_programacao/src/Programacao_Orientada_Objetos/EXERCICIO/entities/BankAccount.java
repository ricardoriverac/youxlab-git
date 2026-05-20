package Programacao_Orientada_Objetos.EXERCICIO.entities;

import javax.xml.namespace.QName;

public class BankAccount {

    private int number;
    private String holder;
    private double balance;


    // GETTERS E SETTERS
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public String getHolder() {
        return holder;
    }

    public void setHolder(String name) {
        this.holder = name;
    }

    public double getBalance() {
        return balance;
    }

    // Conta
    public void deposit(double amount) {
        this.balance += amount;
    }

    public void WithDraw(double amount) {
        this.balance -= 5.00 + amount  ;
    }






}
