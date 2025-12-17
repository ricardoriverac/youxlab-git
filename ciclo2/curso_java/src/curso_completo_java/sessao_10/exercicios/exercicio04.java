package curso_completo_java.sessao_10.exercicios;

/* Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
tela todos os números pares, e também a quantidade de números pares. */


import java.util.Scanner;


public class exercicio04 {

        public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);

            int numero, quantidadePares;

            System.out.print("Quantos numeros voce vai digitar? ");
            numero = sc.nextInt();

            int[] vetor = new int[numero];

            for (int i=0; i<numero; i++) {
                System.out.print("Digite o numero: ");
                vetor[i] = sc.nextInt();
            }

            System.out.println("\nNúmeros pares:");

            quantidadePares = 0;
            for (int i=0; i<numero; i++) {
                if (vetor[i] % 2 == 0) {
                    System.out.printf("%d", vetor[i]);
                    quantidadePares++;
                }
            }

            System.out.printf("\nQuantidade de pares:  %d\n", quantidadePares);

            sc.close();
        }
    }

