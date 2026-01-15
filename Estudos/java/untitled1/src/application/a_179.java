package application;

import application.entities.*;

public class a_179 {
    public static void main(String[] args) {
        FormaAbstrata f1 = new Circulo2(Color.black, 2.0);
        FormaAbstrata f2 = new Retangulo3(Color.blue, 3.0, 4.0);
        System.out.println("Cor do circulo: " + f1.getColor());
        System.out.println("Raio do circulo: " + f1.area());
        System.out.println("Cor do retangulo: " + f2.getColor());
        System.out.println("Area do retangulo: " + f2.area());
    }
}
