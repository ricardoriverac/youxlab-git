package secao_06;

import java.util.Scanner;

public class aula_51 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        int x = 0;
        int y = 4;

        while (x < 3) {
            y += 2;
            x += 1;
        }
        System.out.println(x + "-" + y);
        sc.close();
    }
}
