package Secao6.Aula53;

import java.util.Scanner;

public class aula53 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = 0;
        int y = 4;

        while (x < 3) {
            y += 2;
            x += 1;
            System.out.println(x + "-" + y);
        }
        sc.close();
    }
}
