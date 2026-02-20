package Aula_97.Vetores.Exercicio_Fixacao;

import java.util.Scanner;

public class Exercicio_08 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos elementos vai ter o vetor? ");
        int n = sc.nextInt();

        int[] vetor = new int[n];

        int somaPar = 0;
        int contPar = 0;

        for (int i = 0; i < n; i++) {
            System.out.print("Digite um numero: ");
            vetor[i] = sc.nextInt();

            if (vetor[i] % 2 == 0) {
                somaPar += vetor[i];
                contPar++;
            }
        }

        if (contPar == 0) {
            System.out.println("NENHUM NUMERO PAR");
        } else {
            double media = (double) somaPar / contPar;
            System.out.printf("MEDIA DOS PARES = %.1f%n", media);
        }

        sc.close();
    }
}
