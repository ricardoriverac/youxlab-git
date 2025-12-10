package secao_06;

import java.util.Locale;
import java.util.Scanner;

public class aula_60 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        char resp = 's';
        System.out.print("Digite a temperatura em celsius: ");
        double C = sc.nextDouble();
        double F = 9.0 * C  / 5.0 + 32.0;
        System.out.printf("Equivalente em Fahremheit: %.2f%n", F);
        System.out.printf("Deseja repetir (s/n)? ");
        char resp = sc.next().charAt(0);

        while (resp != 'n'){
            System.out.print("Digite a temperatura em celsius: ");
            C = sc.nextDouble();
            F = 9.0 * C  / 5.0 + 32.0;
            System.out.printf("Equivalente em Fahremheit: %.2f%n", F);
            System.out.printf("Deseja repetir (s/n)? ");
            resp = sc.next().charAt(0);


        }
        sc.close();
    }
}
