package secao6_estruturasRepetitivas;

import java.util.Scanner;

public class testeWhile {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char resp = 's';
        /*  while (resp != 'n') {
            System.out.print("Digite a temperatura em Celsius: ");
            double C = sc.nextDouble();
            double F = 9 * C / 5 + 32;
            System.out.printf("Equivalente em Fahrenheit: %.1f%n", F);
            System.out.print("Deseja repetir (s/n)?");
            resp = sc.next().charAt(0);
        }*/
        do {
            System.out.print("Digite a temperatura em Celsius: ");
            double C = sc.nextDouble();
            double F = 9 * C / 5 + 32;
            System.out.printf("Equivalente em Fahrenheit: %.1f%n", F);
            System.out.print("Deseja repetir (s/n)?");
            resp = sc.next().charAt(0);
        } while(resp != 'n');
    }
}
