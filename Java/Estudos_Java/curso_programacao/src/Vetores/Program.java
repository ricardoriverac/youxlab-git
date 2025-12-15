package Vetores;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Pessoas: ");
        int pessoas = sc.nextInt();
        double[] vect = new double[pessoas];

        for (int i=0; i<pessoas; i++){
            vect[i] = sc.nextDouble();
        }
        double soma = 0;
        for (int i=0; i<pessoas; i++) {
            soma += vect[i];
        }
        double avg = soma / pessoas;
        System.out.printf("AVERAGE HEIGHT: %.2f", avg);

        sc.close();
    }
}
