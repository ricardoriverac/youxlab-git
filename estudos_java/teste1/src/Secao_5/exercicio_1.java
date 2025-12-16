package Secao_5;

import java.util.Scanner;

public class exercicio_1 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = a + b;

        System.out.printf("A soma entre o número %s e o número %d é %d", a, b,c);
    }
}
