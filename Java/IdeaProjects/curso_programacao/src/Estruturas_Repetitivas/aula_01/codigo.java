package Estruturas_Repetitivas.aula_01;

import java.util.Scanner;

public class codigo {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int soma = 0;
        while (x != 0) {
            soma += x;
            x = sc.nextInt();
        }
        System.out.println(soma);


        sc.close();
    }
}
