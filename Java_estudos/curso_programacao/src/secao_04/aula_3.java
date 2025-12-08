package secao_04;

import java.util.Locale;
import java.util.Scanner;

public class aula_3 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        double x;
        x = sc.nextDouble();
        System.out.printf("Voce digitou: %.2f%n", x);

        sc.close();
    }
}
