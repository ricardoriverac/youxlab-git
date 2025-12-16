package Vetores.Exercicios;

import java.util.Locale;
import java.util.Scanner;

public class exer02_soma_vetor {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos números você vai digitar? ");
        int numeros = sc.nextInt();
        double[] vector = new double[numeros];
        for (int i=0; i<numeros; i++) {
            System.out.print("Digite um numero: ");
            vector[i] = sc.nextDouble();
        }
        System.out.print("VALORES = ");
        for (int i=0; i< vector.length; i++) {
            System.out.print(vector[i] + "-> ");
        }
        System.out.println( );

        double soma = 0;
        System.out.print("SOMA = ");
        for (int i=0; i<numeros; i++) {
            soma += vector[i];
        }
        System.out.println(soma);

        System.out.print("MÉDIA = ");
        double media = 0;
        for (int i=0; i<numeros; i++) {
            media = media + vector[i];
        }
        media = media / numeros;
        System.out.printf("%.2f%n", media);







        sc.close();
    }
}
