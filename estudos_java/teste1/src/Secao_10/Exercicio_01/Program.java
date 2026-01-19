package Secao_10.Exercicio_01;

import java.util.Locale;
import java.util.Scanner;

public class Program {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int quantity = sc.nextInt();
        int[] vect = new int[quantity];

        for (int i=0;i<vect.length; i++) {
            int number = sc.nextInt();
            vect[i] = number;
        }

        System.out.println("NÚMEROS NEGATIVOS:");
        for (int i=0; i<vect.length; i++) {
             int valor = vect[i];
            if (valor < 0) {
                System.out.printf("%d%n", vect[i]);
            }
        }

        sc.close();
    }
}
