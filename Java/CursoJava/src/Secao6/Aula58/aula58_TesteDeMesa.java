package Secao6.Aula58;

import java.util.Scanner;

public class aula58_TesteDeMesa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = 3;
        int y = 0;

        for (int i =0; i < x; i++){
            System.out.print(i + ",");
            y += 5;
            System.out.println(y);
        }
        sc.close();
    }
}
