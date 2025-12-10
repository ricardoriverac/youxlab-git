package Estrutura_condicional05.exercicios;

/* Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao
Multiplos", indicando se os valores lidos são múltiplos entre si. Atenção: os números devem poder ser digitados em
ordem crescente ou decrescente.*/

import java.util.Scanner;


public class exercicio_iniciante03 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Digite um número: ");
        int A = sc.nextInt();

        System.out.println("Digite outro número: ");
        int B = sc.nextInt();

        if (A % B == 0 || B % A == 0) {
            System.out.println("São Multíplos");
        }
        else {
            System.out.println("Não são Multíplos");
        }

        sc.close();

    }
}