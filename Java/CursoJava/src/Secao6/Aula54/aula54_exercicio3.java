package Secao6.Aula54;

import java.util.Scanner;

public class aula54_exercicio3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double x = 100;
        double y = 100;
        while (x != y) {
            System.out.print("olha");
            x = Math.sqrt(y);
        }
        sc.close();
    }
}
