package application;

import application.entities.Retangulo;

import java.util.Locale;
import java.util.Scanner;

public class a_70_ex1 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Retangulo retangulo;

        retangulo = new Retangulo();

        System.out.print("Caro usuário, qual a largura do retângulo que você deseja verificar: ");
        retangulo.largura = sc.nextDouble();
        System.out.print("Caro usuário, qual a altura do retângulo que você deseja verificar: ");
        retangulo.altura = sc.nextDouble();

        System.out.println("Caro usuário, a área de seu retângulo é: " + retangulo.area());
        System.out.println("Caro usuário, o perímetro do seu retângulo é: " + retangulo.perimetro());
        System.out.println("Caro usuário, a diagonal do seu retângulo é:  " + retangulo.diagonal());


    }
}
