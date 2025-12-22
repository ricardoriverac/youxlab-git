package secao_10.aula108;

import java.util.Scanner;

public class aula108 {
    static void main() {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [][] math = new int [n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                math[i][j] =  sc.nextInt();
                
            }
        }

        System.out.println("Main diagonal: ");

        for (int i = 0; i < n; i++) {
            System.out.println(math[i][i]);

        }
        System.out.println();

        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (math[i][j] < 0){
                    count++;
                }

            }

        }
        System.out.println("Negative number = " + count);
    }

}
