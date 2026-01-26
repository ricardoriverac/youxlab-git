package Aula_61.Estrutura_repetitiva_para_for;

import java.util.Scanner;

public class Exercicio_07 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int Quantidade_linhas;
        double multiplicacao_quadrada, multiplicacao_cubo;

        System.out.print("Digite a quantidade de linhas: ");
        Quantidade_linhas = sc.nextInt();

        for (double i = 1; i <= Quantidade_linhas ; i ++ ) {

            multiplicacao_quadrada = Math.pow(i, 2);
            multiplicacao_cubo = Math.pow(i, 3);

            System.out.printf("%.0f %.0f %.0f %n", i, multiplicacao_quadrada, multiplicacao_cubo);
        }

    }
}