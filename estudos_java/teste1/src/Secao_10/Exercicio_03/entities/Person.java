package Secao_10.Exercicio_03.entities;

// Classe: usada para criar um modelo de objeto, esse objeto vai ter atributos e comportamentos definidos na classe

public class Person {

    // Atributos da Classe
    // Características de uma classe

    public String name;
    public int age;
    public double height;
    public boolean underage;

    // Construtor
    // Método usado para construir objetos usando algunas valores

    public Person() {}

    public Person(String name, int age, double height) {
        this.name = name;
        this.age = age;
        this.height = height;
        if (age<16) {
            underage = true;
        }
    }

    // Método são comportamentos da classe/objeto
}