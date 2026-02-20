package Aula_97.Vetores.Exercicio_Fixacao;

import java.util.Scanner;

public class Exercicio_05 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int c=0;

        System.out.print("Quantos numeros voce vai digitar: ");
        int n = sc.nextInt();

        int[] vetor = new int[n];

        for (int i=0; i<n; i++) {
            System.out.print("Digite um numero: ");
            vetor[i] = sc.nextInt();
        }

        int maior = vetor[0];

        int posicao = 0;

        for (int i = 1; i < vetor.length; i++) {
            if (vetor[i] > maior) {
                maior = vetor[i];
                posicao = i;
            }
        }

        System.out.println("Maior valor: " + maior);
        System.out.println("Posição do maior: " + posicao);
    }
}
