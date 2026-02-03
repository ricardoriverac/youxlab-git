package Aula_97.Vetores.Exercicio_Fixacao;

import java.util.Scanner;

public class Exercicio_06 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos valores vai ter cada vetor? ");
        int n = sc.nextInt();

        int[] vetor1 = new int[n];
        int[] vetor2 = new int[n];

        System.out.println("Digite os valores do vetor A:");
        for (int i=0; i<vetor1.length; i++) {
            vetor1[i] = sc.nextInt();
        }

        System.out.println("Digite os valores do vetor B:");
        for (int i=0; i<vetor2.length; i++) {
            vetor2[i] = sc.nextInt();
        }

        int sum;
        System.out.println("RESULTADO DA SOMA DOS VETORES:");
        for (int i=0; i<n; i++) {
            sum = vetor2[i] + vetor1[i];
            System.out.println(sum);
        }

    }
}
