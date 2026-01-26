package Secao4.aula37;

import java.util.Locale;
import java.util.Scanner;

public class exercicio5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        int c1,n1,c2,n2;
        double v1,v2,t;

        c1 = sc.nextInt();
        n1 = sc.nextInt();
        v1 = sc.nextDouble();
        c2 = sc.nextInt();
        n2 = sc.nextInt();
        v2 = sc.nextDouble();

        t = n1 * v1 + n2 * v2;
        System.out.println("Código da peça1: " + c1);
        System.out.println("Número da peça1: " + n1);
        System.out.println("Código da peça2: " + c2);
        System.out.println("Número da peça2: " + n2);
        System.out.printf("Valor a ser pago R$%.2f", t);
    }
}
