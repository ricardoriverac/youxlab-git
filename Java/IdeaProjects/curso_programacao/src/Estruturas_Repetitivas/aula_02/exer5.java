package Estruturas_Repetitivas.aula_02;

import java.util.Scanner;

public class exer5 {
    static void main() {
        Scanner sc = new Scanner(System.in);
        int numero = sc.nextInt();
        int fat = 1;

        for (int i=1; i<=numero; i++) {
            fat = fat * i;
        }
        System.out.println(fat);

        sc.close();
    }

}

