package Vetores.Exercicios;

import java.util.Scanner;

public class Exer06_soma_vetores {
    static void main() {
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos vai ter cada vetor: ");
        int qntNumeros = sc.nextInt();
        int[] vetorA = new int[qntNumeros];
        int[] vetorB = new int[qntNumeros];

        System.out.println("Digite os valores do vetor A: ");
        for (int i = 0; i < qntNumeros; i++) {
            vetorA[i] = sc.nextInt();
        }

        System.out.println("Digite os valores do vetor B: ");
        for (int i = 0; i < qntNumeros; i++) {
            vetorB[i] = sc.nextInt();
        }


        int[] vetorC =  new int[qntNumeros];
        System.out.println("VETOR RESULTANTE: ");
        for (int i = 0; i < qntNumeros; i++) {
            vetorC[i] += vetorA[i] + vetorB[i];
        }


        for (int i = 0; i < vetorC.length; i++) {
            System.out.println(vetorC[i]);
        }


        sc.close();
    }
}
