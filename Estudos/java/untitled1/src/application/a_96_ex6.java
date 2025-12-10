package application;

import java.util.Locale;
import java.util.Scanner;

public class a_96_ex6 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Caro usuário quantos valores terão cada vetor? ");
        int quantidadeValores = sc.nextInt();
        int[] vetorA = new int[quantidadeValores];
        int[] vetorB = new int[quantidadeValores];

        for (int i = 0; i < quantidadeValores; i++) {
            System.out.printf("Caro usuário, qual o %do valor de seu vetor A? \n", i+1);
            vetorA[i] = sc.nextInt();
        }
        for (int i = 0; i < quantidadeValores; i++) {
            System.out.printf("Caro usuário, qual o %do valor de seu vetor B? \n", i+1);
            vetorB[i] = sc.nextInt();
        }
        System.out.println("Vetor resultante: ");
        for (int i = 0; i < quantidadeValores; i++) {
            int somaValores = vetorA[i] + vetorB[i];
            System.out.println(somaValores);

        }


    }
}
