package Programacao_Orientada_Objetos.Exercicios.Rectangle.Program;

import Programacao_Orientada_Objetos.Exercicios.Rectangle.entities.rectangle;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter rectangle widht and height: ");
        rectangle.widht = sc.nextDouble();
        rectangle.height = sc.nextDouble();

        System.out.println("Area = " + rectangle.area());
        System.out.println("Perimeter = " + rectangle.perimeter());
        System.out.println("Diagonal = " + rectangle.diagonal());


    }
}
