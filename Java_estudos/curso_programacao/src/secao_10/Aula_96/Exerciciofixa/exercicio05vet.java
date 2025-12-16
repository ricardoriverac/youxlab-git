package secao_10.Aula_96.Exerciciofixa;

import java.util.Locale;
import java.util.Scanner;

public class exercicio05vet {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Quantos numeros voce quer digitar? ");
        int digitarnum = sc.nextInt();
        double[] vetor = new double[digitarnum];


        for (int i = 0; i < digitarnum; i++) {
            System.out.println("Digite um numero: ");
            vetor[i] = sc.nextDouble();
        }
           double maiornumero = vetor[0];
            int posicaomaior = 0;
        for (int i = 0; i < vetor.length; i++) {
            if (vetor[i] > maiornumero){
                maiornumero = vetor[i];
                posicaomaior = i + 1;
            }
        }

        System.out.println("O maior valor é: " +maiornumero );
        System.out.println("A posicao do maior valor é " + posicaomaior);
    }
}
