package curso_completo_java.sessao_08.pratica.exercicio01_pratica.application;

/* Criando um metodo para obtermos os beneficios os beneficios de reaproveitamento e delegação */

import curso_completo_java.sessao_08.pratica.exercicio01_pratica.entities.Triangle;

import java.util.Scanner;
import java.util.Locale;



public class program {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the measures of triangle X: ");

        Triangle x, y;

        x = new Triangle();
        y = new Triangle();

        x.a = sc.nextDouble();
        x.b = sc.nextDouble();
        x.c = sc.nextDouble();


        System.out.println("Enter the measures of triangle Y: ");
        y.a = sc.nextDouble();
        y.b = sc.nextDouble();
        y.c = sc.nextDouble();

        double areaX = x.area();
        double areaY = y.area();

        System.out.printf("Triangle X area: %.4f%n", areaX);
        System.out.printf("Triangle Y area: %.4f%n", areaY);

        if (areaX > areaY) {
        }
    }
}