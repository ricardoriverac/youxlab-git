package curso_completo_java.sessao_10.exercicios;

/* Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.*/

import java.util.Locale;
import java.util.Scanner;

public class exercicio07 {

        public static void main(String[] args) {

            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

            int numeros;
            double soma, media;

            System.out.print("Quantos números vai ter o vetor?: ");
            numeros = sc.nextInt();

            double[] vetor = new double[numeros];

            for (int i=0; i<numeros; i++) {
                System.out.print("Digite um numero: ");
                vetor[i] = sc.nextDouble();
            }

            soma = 0;
            for (int i=0; i<numeros; i++) {
                soma = soma + vetor[i];
            }

            media = soma / numeros;

            System.out.printf("\nMédia do vetor: %.3f\n", media);
            System.out.println("Elementos a baixo da média: ");

            for (int i=0; i<numeros; i++) {
                if (vetor[i] < media) {
                    System.out.printf("%.1f\n", vetor[i]);
                }
            }

            sc.close();
        }
    }

