package Vetores.Exercicios.exer03.entities;

import java.util.Locale;
import java.util.Scanner;

public class Person {
    private String name;
    private int idade;
    private double altura;

    public Person(String name, double altura, int idade) {
        this.name =name;
        this.idade= idade;
        this.altura= altura;
    }

    public Person() {
    }
    // getters setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public String toSring(){
        return "Nome: "
                + name
                + "Idade: "
                + idade
                + "Altura: "
                + altura;
    }

    // person


}
