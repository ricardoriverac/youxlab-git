package Programacao_Orientada_Objetos.Triangulo;

import java.util.Locale;
import java.util.Scanner;

public class codigo {
    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double xA, xB, xC, yA, yB, yC;
        System.out.println("Digite os lados do triângulo X");
        xA = sc.nextDouble();
        xB = sc.nextDouble();
        xC = sc.nextDouble();

        System.out.println("Digite os lados do triângulo Y");
        yA = sc.nextDouble();
        yB = sc.nextDouble();
        yC = sc.nextDouble();

        double p = (xA + xB + xC) / 2.0;
        double areaX = Math.sqrt(p * (p - xA) * (p - xB) * (p - xC));

        p = (yA + yB + yC) / 2.0;
        double areaY = Math.sqrt(p * (p - yA) * (p - yB) * (p - yC));

        System.out.printf("Área do triângulo X = %.4f%n", areaX);
        System.out.printf("Área do triângulo Y = %.4f%n", areaY);

        if (areaX > areaY) {
            System.out.println("Maior área: X");
        }
        else {
            System.out.println("Maior área: Y");
        }

        sc.close();
    }
}
