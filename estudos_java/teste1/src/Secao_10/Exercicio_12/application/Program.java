package Secao_10.Exercicio_12.application;

import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("How many lines do you want?");
        int l = sc.nextInt();
        System.out.print("How many columns do you want?");
        int c = sc.nextInt();
        int[][] mat = new int[l][c];

        for (int i=0 ; i<l ; i++) {
            System.out.printf("Numbers from the %d°line: ", i + 1);
            for (int j = 0; j < c ; j++) {
                int number = sc.nextInt();
                mat[i][j] = number;
            }
        }

        System.out.print("Choose a number:");
        int chosenNumber = sc.nextInt();

        for (int i = 0; i < l; i++) {
            for (int j = 0; j < c; j++) {
                if (chosenNumber == mat[i][j]) {
                    System.out.println("Position: " + (i+1) + "," + (j+1));
                    if (j-1>=0) {
                        System.out.println("Left: " + mat[i][j - 1]);
                    }
                    if (j+1<c) {
                        System.out.println("Right: " + mat[i][j + 1]);
                    }
                    if (i-1>=0) {
                        System.out.println("Up: " + mat[i - 1][j]);
                    }
                    if (i+1<l) {
                        System.out.println("Down: " + mat[i + 1][j]);
                    }
                }
            }
        }

        sc.close();
    }
}
