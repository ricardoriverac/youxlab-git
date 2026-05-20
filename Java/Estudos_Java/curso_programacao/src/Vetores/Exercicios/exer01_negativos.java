package Vetores.Exercicios;

import java.util.Scanner;

public class exer01_negativos {
    static void main() {
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos números serão digitados? ");
        int negativos = 0, numeros = sc.nextInt();
        int[] vect = new int[numeros];
        for (int i=0; i<numeros; i++) {
            System.out.print("Digite um número: ");
            vect[i] = sc.nextInt();
        }

        System.out.println("NÚMEROS NEGATIVOS:");

        for (int i=0; i<numeros; i++) {
            if (vect[i] < 0) {
                System.out.println(vect[i]);
            }
        }


        sc.close();
    }
}
