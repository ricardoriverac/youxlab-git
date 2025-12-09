package Estruturas_Repetitivas.aula_02;

import java.util.Scanner;

public class exer6 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite um número para saber seus divisores:");
        int numero = sc.nextInt();
        for (int i = numero; i<=numero; i--) {
            if (numero % i == 0) {
                System.out.println(i);
            }
        }
        sc.close();
    }
}
