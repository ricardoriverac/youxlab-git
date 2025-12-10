package Estruturas_Repetitivas.do_while_03;

import java.util.Locale;
import java.util.Scanner;

public class codigo {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        char resposta;
        do {
            System.out.print("Digite a temperatura em Celsius: ");
            double C = sc.nextDouble();
            double F = 9.0 * C / 5.0 + 32.0;
            System.out.printf("Equivalente a Fahrenheit: %.1f%n", F);
            System.out.print("Deseja repetir (s/n)? ");
            resposta = sc.next().charAt(0);
        } while (resposta != 'n');
        sc.close();
    }
}
