package Secao5.Aula44;

import java.util.Scanner;

public class aula44_exercicio2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n;
        System.out.println("Digite um número: ");
        n = sc.nextInt();
        if (n % 2 == 0) {
            System.out.println("Par");
        } else {
            System.out.println("Ímpar");
        }
    }
}