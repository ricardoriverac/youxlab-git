package Programacao_Orientada_Objetos.Membros_Estaticos.application;

import Programacao_Orientada_Objetos.Membros_Estaticos.util.Calculator;

import java.util.Locale;
import java.util.Scanner;

public class Codigo {
    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter radius: ");
        double radius = sc.nextDouble();

        double circum = Calculator.circumference(radius);

        double volum = Calculator.volume(radius);

        System.out.printf("Circumference: %.2f%n", circum);
        System.out.printf("Volume: %.2f%n", volum);
        System.out.printf("PI value: %.2f%n", Calculator.PI);

        sc.close();
    }

}
