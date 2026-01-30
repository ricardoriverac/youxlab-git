package Secao6.Aula59;

import java.util.Scanner;

public class Aula59_exercicio2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = 4;
        int y = 0;
        for (int i =0; i<x; i++) {
            y += i;
        }
        System.out.println(y);
        sc.close();
    }
}
