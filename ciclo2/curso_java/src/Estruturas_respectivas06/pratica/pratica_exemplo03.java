package Estruturas_respectivas06.pratica;

/*Fazer um programa que lê um valor
inteiro N e depois N números inteiros.
Ao final, mostra a soma dos N números
lidos*/

import java.util.Scanner;

public class pratica_exemplo03 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int soma = 0;

        for (int i=0; i<n; i++) {
            int x = sc.nextInt();
            soma = soma + x;

        }

        System.out.println(soma);

        sc.close();

    }
}
