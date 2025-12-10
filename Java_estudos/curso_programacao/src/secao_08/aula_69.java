package secao_08;

import java.util.Locale;
import java.util.Scanner;

public class aula_69 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double xA, xB, xC, yA, yB, yC;

        System.out.println("Enter the measures of triangle X: ");
        xA = sc.nextDouble();
        xB = sc.nextDouble();
        xC = sc.nextDouble();
        System.out.println("Enter the measures of triangle Y: ");
        yA = sc.nextDouble();
        yB = sc.nextDouble();
        yC = sc.nextDouble();

        double p = (xA + xB + xC) / 2.0;
        double areaX = Math.sqrt(p * (p - xA) * (p - xB) * (p - xC));

        p = (xA + xB + xC) / 2.0;
        double areaY = Math.sqrt(p * (p - xA) * (p - xB) * (p - xC));

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
