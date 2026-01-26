package Secao4.aula37;

import java.util.Locale;
import java.util.Scanner;

public class exercicio3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        int A, B, C, D, E;
        System.out.println("Digite os valores dos produtos: ");
        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();
        D = sc.nextInt();
        E = (A * B - C * D);

        System.out.println("A diferença entre os produtos são de: "+ E);

    }
}
