package Aula_97.Vetores.Exercicio_Fixacao;

import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class Exercicio_07 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos elementos vai ter o vetor? ");
        int n = sc.nextInt();

        double[] vetor = new double[n];

        for (int i=0; i<n; i++) {
            System.out.print("Digite um numero: ");
            vetor[i] = sc.nextDouble();
        }

        double media = Arrays.stream(vetor).sum() / n;

        System.out.printf("MEDIA DO VETOR = %.3f %n", media);

        System.out.println("ELEMENTOS ABAIXO DA MEDIA:");

        for (int i=0; i<n; i++) {
            if (vetor[i] < media) {
                System.out.printf("%.1f  %n",vetor[i]);
            }
        }

    }
}
