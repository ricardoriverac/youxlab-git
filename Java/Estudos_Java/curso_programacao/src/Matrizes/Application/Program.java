package Matrizes.Application;

import java.util.Scanner;

public class Program {

    static void main() {

        Scanner sc = new Scanner(System.in);

        int tamanhoMatriz = sc.nextInt();
        int[][] mat = new int[tamanhoMatriz][tamanhoMatriz];

        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                mat[i][j] = sc.nextInt();
            }
        }

        System.out.println("Main diagonal:");

        for (int i = 0; i < mat.length; i++) {
            System.out.print(mat[i][i] + " ");
        }
        System.out.println();
        int countNegative = 0;
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] < 0) {
                    countNegative++;
                }
            }
        }

        System.out.println("Negative numbers: " + countNegative);

        sc.close();
    }
}
