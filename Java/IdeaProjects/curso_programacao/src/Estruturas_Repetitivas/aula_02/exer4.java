package Estruturas_Repetitivas.aula_02;

import java.util.Scanner;

public class exer4 {
    static void main() {

        Scanner sc = new Scanner(System.in);

        System.out.println("Quantidade de operações:");
        int qnt_numeros = sc.nextInt();
        int numerador=0, denominador=0;
        for (int i = 0; i<qnt_numeros; i++) {
            int par1 = sc.nextInt();
            int par2 = sc.nextInt();
            if (par2 == 0) {
                System.out.println("Divisão impossível");
            }
            else {
                numerador += par1;
                denominador += par2;
                double divisao = (double) numerador / denominador;
                System.out.printf("%.1f%n",divisao);
            }
        }
        sc.close();
    }
}
