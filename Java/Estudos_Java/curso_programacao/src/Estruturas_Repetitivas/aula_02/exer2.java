package Estruturas_Repetitivas.aula_02;

import java.util.Scanner;

public class exer2 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite um número inteiro:");
        int qnt_numeros = sc.nextInt();
        int numero,in = 0, out = 0;

        for(int i = 0; i<qnt_numeros; i ++) {
            numero = sc.nextInt();
            if (10 >= numero && numero <= 20) {
                in++;
            }
            else {
                out++;
            }
        }
        System.out.println(in + " Dentro");
        System.out.println(out + " Fora");
        sc.close();
    }
}
