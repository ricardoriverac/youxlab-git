package Estrutura_Condicional.aula_01;

import java.util.Scanner;

public class exer3 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int A, B;
        System.out.println("Primeiro número inteiro:");
        A = sc.nextInt();
        System.out.println("Segundo número inteiro:");
        B = sc.nextInt();

        if (A % B == 0 || B % A == 0){
            System.out.println("São multiplos");
        }
        else {
            System.out.println("São multiplos");
        }
    }
}
