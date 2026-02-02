package curso_completo_java.sessao_10.exercicios;

/*Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos*/

import java.util.Locale;
import java.util.Scanner;


public class exercicio01 {

        public static void main(String[] args) {

            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

            int n;
            double soma, media;

            System.out.print("Quantos números você vai digitar? ");
            n = sc.nextInt();

            double[] vetor = new double[n];

            for (int i=0; i<n; i++) {
                System.out.print("Digite um numero: ");
                vetor[i] = sc.nextDouble();
            }

            soma = 0;
            for (int i=0; i<n; i++) {
                soma = soma + vetor[i];
            }

            media = soma / n;

            System.out.print("Valores: ");

            for (int i=0; i<n; i++) {
                if (vetor[i] < 0){
                    System.out.printf("%.1f  \n", vetor[i]);
                }

            }

            System.out.printf("soma: %.2f\n", soma);
            System.out.printf("média: %.2f\n", media);

            sc.close();
        }
    }

