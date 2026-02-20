package Aula_109.Matrizes.Exercicio_Fixacao;

import java.util.Scanner;

public class Main_01 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um valor númerico: ");
        int n = sc.nextInt();

        int c = 0;

        int[][] matriz = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.println("Digite um valor: ");
                matriz[i][j] = sc.nextInt();
            }
        }
        System.out.println("Números na diagonal: ");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j == i) {
                    System.out.print(matriz[i][j]+ " ");
                }

                if (matriz[i][j] < 0) {
                    c++;
                }
            }
        }

        System.out.printf("%nNúmeros negativos = %d", c);

    }
}
