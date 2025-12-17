package curso_completo_java.sessao_05.exercicios;

/* Fazer um programa para ler um número
inteiro e dizer se este número é par ou ímpar. */

import java.util.Scanner;

public class exercicio_iniciante02 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Digite um número : ");
        int Numero = sc.nextInt();

        if (Numero % 2 == 0) {
            System.out.println("Seu número é par");
        }
        else {
            System.out.println("Seu número é impar");
        }

        sc.close();
    }

    }

