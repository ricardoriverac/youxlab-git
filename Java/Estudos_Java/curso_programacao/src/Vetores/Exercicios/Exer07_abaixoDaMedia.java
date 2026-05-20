package Vetores.Exercicios;

import java.util.Locale;
import java.util.Scanner;

public class Exer07_abaixoDaMedia {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        System.out.print("Quantos elementos terá o vetor? ");
        int qntNumeros = sc.nextInt();
        double[] vetorNumeros =  new double[qntNumeros];

        for (int i = 0; i < qntNumeros; i++) {
            System.out.print("Digite um número: ");
            vetorNumeros[i] = sc.nextDouble();
        }

        double mediaVetor = 0;
        for (int i = 0; i < vetorNumeros.length; i++) {
            mediaVetor += vetorNumeros[i];
        }
        mediaVetor = mediaVetor / vetorNumeros.length;
        System.out.printf("MEDIA DO VETOR = %.3f%n", mediaVetor);

        System.out.println("ELEMENTOS ABAIXO DA MEDIA: ");
        for (int i = 0; i < vetorNumeros.length; i++) {
            if (vetorNumeros[i] < mediaVetor) {
                System.out.println(vetorNumeros[i]);
            }
        }

        sc.close();
    }
}
