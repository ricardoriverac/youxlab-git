package Topios_basios_java.Funcoes;

import java.util.Scanner;

public class codigo {
    static void main() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite tres números inteiros: ");
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();

        int maior = max(num1, num2, num3);

        showResult(maior);

        sc.close();
    }

    public static int max(int x, int y, int z) {
        int aux;
        if (x > y && x > z) {
            aux = x;
        } else if (y > z) {
            aux = y;
        } else {
            aux = z;
        }
        return aux;

    }

    public static void showResult(int valor) {
        System.out.println("Maior = " + valor);
    }

}