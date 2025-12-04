package application;

import application.entities.Calculator;

import java.util.Locale;
import java.util.Scanner;

public class a_76_2 {
    public static void main(String[] args) {
            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

            Calculator calculator = new Calculator();
            System.out.print("Caro usuário, por favor insira o raio de sua circunferência: ");
            double raio = sc.nextDouble();

            double c = calculator.circunferencia(raio);
            double v = calculator.volume(raio);

            System.out.printf("Circunferência: %.2f\n", c);
            System.out.printf("Volume: %.2f\n", v);
            System.out.printf("PI value: %.2f\n", calculator.PI);

            sc.close();
        }


    }

