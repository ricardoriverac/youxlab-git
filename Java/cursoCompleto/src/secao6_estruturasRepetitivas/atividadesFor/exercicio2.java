package secao6_estruturasRepetitivas.atividadesFor;

import java.util.Scanner;

public class exercicio2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int entrou = 0;
        int saiu = 0;
        for (int i=10; i < 20; i++) {
            if (10 <= x && x <= 20 ) {
                entrou++;
            }
            else {
                saiu++;
            }
            x = sc.nextInt();
        }
        System.out.println(entrou + " in\n" + saiu + " out");

    }
}
