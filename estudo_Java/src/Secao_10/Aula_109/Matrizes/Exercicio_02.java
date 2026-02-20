package Aula_109.Matrizes;

import java.util.Scanner;

public class Exercicio_02 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[][] matriz = new int[3][2];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 2; j++) {
                System.out.print("Digite um valor: ");
                matriz[i][j] = sc.nextInt();
            }
        }

        int sum = 0;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 2; j++) {
                System.out.print(matriz[i][j] + " ");
                sum += matriz[i][j];
            }
        }

        System.out.printf("%nSoma de todos os valores: %d", sum);

    }
}
