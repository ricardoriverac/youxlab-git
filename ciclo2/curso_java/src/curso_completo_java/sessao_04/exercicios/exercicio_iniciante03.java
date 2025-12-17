package curso_completo_java.sessao_04.exercicios;

/* Fazer um programa para ler quatro valores inteiros A, B, C e D.
 A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e
 D segundo a fórmula: DIFERENCA = (A * B - C * D)
 */

import java.util.Scanner;

public class exercicio_iniciante03 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int A, B, C, D, Diferenca;

        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();
        D = sc.nextInt();

        Diferenca = A * B - C * D;

        System.out.printf("Diferença = %d", Diferenca);


    }
}
