package Topios_basios_java.Operadores_bitwise;

import java.util.Scanner;

public class codigo {
    static void main() {

        int n1 = 89;
        int n2 = 60;
        System.out.println(n1 & n2);
        System.out.println(n1 | n2);
        System.out.println(n1 ^ n2);

        System.out.println("--------------------------------");

        Scanner sc = new Scanner(System.in);
        int mask = 0b100000;
        int n = sc.nextInt();

        if ((n & mask) != 0) {
            System.out.println("6th bit is True!");
        }
        else {
            System.out.println("6th bit is False!");
        }
    }
}
