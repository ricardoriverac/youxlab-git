package Estrutura_Condicional.aula_01;

import java.util.Scanner;

public class exer1 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int A;
        System.out.println("Digite um número inteiro:");
        A = sc.nextInt();

        if (A > 0) {
            System.out.println("Número positivo!");
        }
        else {
            System.out.println("Número negativo!");
        }
    }
}
