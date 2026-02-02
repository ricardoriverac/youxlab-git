package curso_completo_java.sessao_10.exercicios;

/* Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
digitado, mostrar a mensagem "NENHUM NUMERO PAR" */

import java.util.Locale;
import java.util.Scanner;

public class exercicio08 {

        public static void main(String[] args) {

            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

            int numeros, somaPares = 0, numerosPares = 0;
            double mediaPares;

            System.out.print("Quantos números o vetor vai ter?: ");
            numeros = sc.nextInt();

            int[] vetor = new int[numeros];

            for (int i=0; i<numeros; i++) {
                System.out.print("Digite um número: ");
                vetor[i] = sc.nextInt();
            }

            for (int i=0; i<numeros; i++) {
                if (vetor[i] % 2 == 0) {
                    somaPares = somaPares + vetor[i];
                    numerosPares++;
                }
            }

            if (numerosPares == 0) {
                System.out.println("Nenhum número par");
            }
            else {
                mediaPares = (double)somaPares / numerosPares;

                System.out.printf("Média dos pares: %.1f\n", mediaPares);
            }

            sc.close();
        }
    }

