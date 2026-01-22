package Aula_61.Estrutura_repetitiva_para_for;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio_03 {
    public static void main(String[] args) {


        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int Quantidade_repeticao;

        System.out.print("Digite a quantidade que deseja: ");
        Quantidade_repeticao = sc.nextInt();

        for (int i = 0; i < Quantidade_repeticao; i++ ) {

            double valor1, valor2, valor3, resultado;

            System.out.println("Digite o 1º valor: ");
            valor1 = sc.nextDouble();
            valor1 = valor1 * 2;

            System.out.println("Digite o 2º valor: ");
            valor2 = sc.nextDouble();
            valor2 = valor2 * 3;

            System.out.println("Digite o 3º valor: ");
            valor3 = sc.nextDouble();
            valor3 = valor3 * 5;

            resultado = (valor1 + valor2 + valor3) / 10;
            System.out.printf("resultado: %.1f %n", resultado);

            System.out.println("======================================");
        }

    }
}