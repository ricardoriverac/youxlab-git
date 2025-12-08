package Estrutura_sequencial04.exercicios;

/* Faça um programa para ler dois valores inteiros, e depois mostrar
na tela a soma desses números com uma mensagem
 */

import java.util.Scanner;

    public class exercicio_iniciante01 {

        public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);

            int A, B, soma;

            A = sc.nextInt();
            B = sc.nextInt();

            soma = A + B;

            System.out.println("Resultado da soma = " + soma);

            sc.close();
        }
    }

