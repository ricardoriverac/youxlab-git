package Aula_61.Estrutura_repetitiva_para_for;

import java.util.Scanner;

public class Exercicio_06 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int numero, calculo = 1;

        System.out.print("Digite um número: ");
        numero = sc.nextInt();


        for (int i = numero; i >= 1; i--) {

            if (i == numero) {
                System.out.printf("O número %d e divisivel por: ", i);
            }

            if (numero % i == 0) {
                System.out.print(i + " ");
            }

        }

    }
}