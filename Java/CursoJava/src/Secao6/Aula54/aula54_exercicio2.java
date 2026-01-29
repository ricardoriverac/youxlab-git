package Secao6.Aula54;

import java.util.Scanner;

public class aula54_exercicio2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = 2;
        int y = 0;
        while (x < 60) {
            System.out.println(x);
            x = x * 2;
            y = y + 10;
        }
        sc.close();
    }
}
