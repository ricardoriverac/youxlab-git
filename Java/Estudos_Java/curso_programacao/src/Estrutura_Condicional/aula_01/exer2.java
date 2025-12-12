package Estrutura_Condicional.aula_01;

import java.util.Scanner;

public class exer2 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int A;
        System.out.println("Digite um número inteiro:");
        A = sc.nextInt();

        if (A % 2 == 0) {
            System.out.println("Número Par!");
        }
        else {
            System.out.println("Número Ímpar");
        }
    }
}
