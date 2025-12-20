package secao_10.aula96.Exerciciofixa;

import java.util.Locale;
import java.util.Scanner;

public class exercicio06vet {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Quantos valores vai ter cada vetor: ");
        int vetorvalor = sc.nextInt();

        double[] vetorA = new double[vetorvalor];
        double[] vetorB = new double[vetorvalor];
        double[] vetorC = new double[vetorvalor];


        System.out.println("Digite os valores do vetor A");


        for (int i = 0; i < vetorvalor; i++) {
            vetorA[i] = sc.nextDouble();
        }

        System.out.println("Digite os valores do vetor B: ");
        for (int i = 0; i < vetorvalor; i++) {
            vetorB[i] = sc.nextDouble();
        }

        System.out.println("Vetor resultante: ");
        for (int i = 0; i < vetorvalor; i++) {
            vetorC[i] = vetorA[i] + vetorB[i];

        }

        for (int i = 0; i < vetorC.length; i++) {
            System.out.println(vetorC[i]);

        }

        sc.close();


        }


    }
