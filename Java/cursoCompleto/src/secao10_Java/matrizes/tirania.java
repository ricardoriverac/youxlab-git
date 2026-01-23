package secao10_Java.matrizes;

import java.util.Arrays;
import java.util.Scanner;

public class tirania {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite o número de linhas: ");
        int m = sc.nextInt();
        System.out.print("Digite o número de colunas: ");
        int n = sc.nextInt();
        int[][] numMatriz = new int[m][n];
        for (int i=0; i<numMatriz.length; i++) {
            for (int j=0; j<numMatriz[i].length; j++) {
                numMatriz[i][j] = sc.nextInt();
            }
        }
        System.out.print("Digite o número que prefere: ");
        int x = sc.nextInt();
        for (int i = 0; i < numMatriz.length; i++){
            for (int j = 0; j < numMatriz.length; j++){
                if (numMatriz[i][j] == x){
                    System.out.println("Número digitado: " + x);
                    System.out.println("Posição " +  i + ", "+ j);
                    if ( j < 0) {
                        System.out.println("Número a esquerda: " + numMatriz[i][j-1]);
                    }
                    else {
                        System.out.println("Não há números a esquerda.");
                    }
                    if (j < numMatriz[i].length - 1) {
                        System.out.println("Número a direita: " + numMatriz[i][j + 1]);
                    }
                    else {
                        System.out.println("Não há números a direita.");
                    }
                    if (i < 0) {
                        System.out.println("Número acima: " + numMatriz[i - 1][j]);
                    }
                    else {
                        System.out.println("Não há números acima.");
                    }
                    if (i < numMatriz.length - 1) {
                        System.out.println("Número abaixo" + numMatriz[i + 1][j]);
                    }
                    else {
                        System.out.println("Não há números abaixo.");
                    }
                }
            }
        }


    }
}
