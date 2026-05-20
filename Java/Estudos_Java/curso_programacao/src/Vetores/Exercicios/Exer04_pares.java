package Vetores.Exercicios;

import java.util.Scanner;

public class Exer04_pares {
    static void main() {
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos números você vai digitar? ");
        int numeros = sc.nextInt();
        int[] pares = new int[numeros];

        for (int i = 0; i < numeros; i++) {
            System.out.print("Digite um número: ");
            pares[i] = sc.nextInt();
        }
        int numerosPares = 0;
        System.out.println("NUMEROS PARES: ");
        for (int i = 0; i < pares.length; i++) {
            if (pares[i] % 2 == 0){
                numerosPares++;
                System.out.print(pares[i] + " ");
            }
        }
        System.out.println();
        System.out.print("QUANTIDADE DE PARES: " + numerosPares);


        sc.close();
    }
}
