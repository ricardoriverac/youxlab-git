package secao_08.produto.Aula77;

import java.util.Locale;
import java.util.Scanner;

import static secao_08.produto.Aula77.calculadora.circunference;
import static secao_08.produto.Aula77.calculadora.volume;

public class application {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        calculadora clc = new calculadora();

        System.out.println("Enter radius: ");
        double radius = sc.nextDouble();

        double c = circunference(radius);
        double v = volume(radius);
        System.out.printf("Circumference: %.2f%n", c);
        System.out.printf("Volume: %.2f%n", v);

        sc.close();
    }
}
