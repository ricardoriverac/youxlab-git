package Secao8.Aula78;

import Secao8.Aula78.util.calculator;

import java.util.Locale;
import java.util.Scanner;

// TODO EXEMPLO QUE ESTA SENDO PRATICADO NA AULA 78 ESTAVA SENDO APLICADO NESSE PROGRAMA//

public class aula78_pt1 {
    public static final double PI = 3.14159;

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter radius: ");
        double radius = sc.nextDouble();

        double c = calculator.circumference(radius);

        double v = calculator.volume(radius);

        System.out.printf("Circumference: %.2f\n", c);
        System.out.printf("Volume: %.2f\n", v);
        System.out.printf("PI value: %.2f\n", calculator.PI);
        sc.close();
    }

    }

