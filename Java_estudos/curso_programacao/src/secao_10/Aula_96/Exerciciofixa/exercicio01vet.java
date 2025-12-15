package secao_10.Aula_96.Exerciciofixa;

import java.util.Locale;
import java.util.Scanner;

public class exercicio01vet {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        System.out.println("Quantos números você deseja digitar? ");
        int N = sc.nextInt();

        double[] vect = new double[N];
        for (int i = 0; i < N; i++) {
            vect[i] = sc.nextDouble();

        }

    }
}
