package Programacao_Orientada_Objetos.Triangulo.codigo_principal;

import Programacao_Orientada_Objetos.Triangulo.entities.triangulo;

import java.util.Locale;
import java.util.Scanner;

public class codigo {
    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        triangulo x, y;
        x = new triangulo();
        y = new triangulo();

        System.out.println("Digite os lados do triângulo X");
        x.a = sc.nextDouble();
        x.b = sc.nextDouble();
        x.c = sc.nextDouble();

        System.out.println("Digite os lados do triângulo Y");
        y.a = sc.nextDouble();
        y.b = sc.nextDouble();
        y.c = sc.nextDouble();

        double areaX = x.area();
        double areaY = y.area();

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
