package Estruturas_Repetitivas.aula_01;

import java.util.Scanner;

public class exer2 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int x, y;
        x = sc.nextInt();
        y = sc.nextInt();

        while (x != 0 || y != 0) {
            if (x > 0 && y > 0) {
                System.out.println("primeiro");
            }
            else if (x < 0 && y > 0) {
                System.out.println("segundo");
            }
            else if (x < 0 && y < 0) {
                System.out.println("terceiro");
            }
            else if (x > 0 && y < 0) {
                System.out.println("quarto");
            }
            else if (x == 0 && y != 0 || y == 0 && x != 0) {
                System.out.println(" ");
            }
            x = sc.nextInt();
            y = sc.nextInt();
        }
    }
}
