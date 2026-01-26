package Secao4.aula37;

import java.util.Locale;
import java.util.Scanner;

public class exercicio4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        int n,h;
        double v,t;

        n = sc.nextInt();
        h = sc.nextInt();
        v = sc.nextDouble();
        t = h * v;
        System.out.println("--------DADOS-----------");
        System.out.println("NUMBER: " +n);
        System.out.printf("SALARY: U$%.2f", t);
    }
}
