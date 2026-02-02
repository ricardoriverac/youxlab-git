package curso_completo_java.sessao_10.exercicios;

/* Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
o vetor C gerado. */

import java.util.Locale;
import java.util.Scanner;

public class exercicio06 {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int numeros ;

        System.out.print("Quantos números você vai digitar?: ");
        numeros = sc.nextInt();

        int[] A = new int[numeros];
        int[] B = new int[numeros];
        int[] C = new int[numeros];

        System.out.println("Digite os números do vetor A:");

        for (int i=0; i<numeros; i++) {
            A[i] = sc.nextInt();
        }

        System.out.println("Digite os números do vetor B:");

        for (int i=0; i<numeros; i++) {
            B[i] = sc.nextInt();
        }

        for (int i=0; i<numeros; i++) {
            C[i] = A[i] + B[i];
        }

        System.out.println("Vetor resultante:");

        for (int i=0; i<numeros; i++) {
            System.out.printf("%d\n", C[i]);
        }

        sc.close();





    }
}
