package Aula_97.Vetores.Exercicio_Fixacao;

import java.util.Scanner;

public class Exercicio_01 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos numeros voce vai digitar? ");
        int n = sc.nextInt();

        int[] vetor = new int[n];
        int[] vetorNegativo = new int[n];

        for (int i=0; i<n; i++) {
            System.out.print("Digite um numero: ");
            vetor[i] = sc.nextInt();
            if (vetor[i] < 0) {
                vetorNegativo[i] = vetor[i];
            }
        }

        for (int i=0; i < vetorNegativo.length; i++) {
            if (vetorNegativo[i] != 0){
                System.out.println(vetorNegativo[i]);
            }

        }

    }
}