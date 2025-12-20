package secao_10.aula96.Exerciciofixa;

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
            System.out.print("Digite um número: ");
            vect[i] = sc.nextDouble();
        }
        System.out.println("Números negativos: ");

        for (int i = 0; i < N; i++) {
            if (vect[i] < 0){
                System.out.println(vect[i]);

            }

            sc.close();

        }

    }
}
