package secao_08.codigo_principal;

import secao_08.entities.triangulo;

import java.util.Locale;
import java.util.Scanner;

public class aula_69 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        triangulo x, y;
        x = new triangulo();
        y = new triangulo();

        System.out.println("Enter the measures of triangle X: ");
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
        System.out.printf("Triangle X area: %.4f%n", areaY);

        if (areaX > areaY){
            System.out.println("Lager area: X");
        }else {
            System.out.println("Lager area: Y");

        }
        sc.close();





    }
}
