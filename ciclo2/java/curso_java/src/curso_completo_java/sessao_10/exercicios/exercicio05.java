package curso_completo_java.sessao_10.exercicios;

/* Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
considerando a primeira posição como 0 (zero) */

import java.util.Locale;
import java.util.Scanner;

public class exercicio05 {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int numeros, posicaoMaior;
        double maiorValor;

        System.out.print("Quantos numeros voce vai digitar? ");
        numeros = sc.nextInt();

        int[] vetor = new int[numeros];

        for (int i = 0; i < numeros; i++) {
            System.out.print("Digite o numero: ");
            vetor[i] = sc.nextInt();
        }

        maiorValor = vetor[0];
        posicaoMaior = 0;

        for (int i = 1; i < numeros; i++) {
            if (vetor[i] > maiorValor) {
                maiorValor = vetor[i];
                posicaoMaior = i;
            }

        }

        System.out.printf("Maior valor: %.1f\n", maiorValor);
        System.out.printf("Posição do maior valor: %d", posicaoMaior);
    }

}
