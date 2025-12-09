package secao_06;

import java.util.Scanner;

public class exercicio5for {
    static void main() {
         Scanner sc = new Scanner(System.in);
            int numero = sc.nextInt();
            int fat = 1;

            for (int i=1; i<=numero; i++) {
                fat = fat * i;
            }
            System.out.println(fat);

            sc.close();
        }

    }

