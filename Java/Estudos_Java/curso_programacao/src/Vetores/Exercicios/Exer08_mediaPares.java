package Vetores.Exercicios;

import java.util.Scanner;

public class Exer08_mediaPares {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Quantos elementos terá o vetor? ");
        int qntNumeros = sc.nextInt();
        int[] vetorNumeros = new int[qntNumeros];

        for (int i = 0; i < qntNumeros; i++) {
            System.out.print("Digite um número: ");
            vetorNumeros[i] = sc.nextInt();
        }

        double somaVetor = 0;
        int countPares = 0;
        for (int i = 0; i < vetorNumeros.length; i++) {
            if (vetorNumeros[i] % 2 == 0) {
                somaVetor += vetorNumeros[i];
                countPares++;
            }

        }
        if (somaVetor == 0) {
            System.out.println("NENHUM NÚMERO PAR");
        }
        else {
            System.out.printf("MEDIA DOS PARES = %.1f.%n", somaVetor / countPares);
        }


        sc.close();
    }
}
