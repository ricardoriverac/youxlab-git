package secao_06;

import java.util.Scanner;

public class exercicio4for {
    static void main() {
        System.out.println("Digite a quantidade de operações");
        Scanner sc = new Scanner(System.in);
        int numero = sc.nextInt();

        for (int i=0; i<numero; i++) {

            int primeiro = sc.nextInt();
            int segundo = sc.nextInt();

            if (segundo == 0) {
                System.out.println("Divisao impossivel");
            }
            else {
                double div = (double) primeiro / segundo;
                System.out.printf("%.1f%n", div);
            }
        }

        sc.close();
        }
    }