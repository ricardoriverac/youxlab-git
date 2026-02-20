package Aula_61.Estrutura_repetitiva_para_for;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio_04 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double Valor_numerador, Valor_denominador, Quantidade_pares_numericos, resultado;

        System.out.print("Digite a quantidade que deseja calcular: ");
        Quantidade_pares_numericos = sc.nextDouble();

        for (int i = 0; i < Quantidade_pares_numericos; i ++) {
            System.out.print("Digite o valor do Numerador: ");
            Valor_numerador = sc.nextDouble();

            System.out.print("Digite o valor do Denominador: ");
            Valor_denominador = sc.nextDouble();

            if (Valor_denominador != 0) {
                resultado = Valor_numerador / Valor_denominador;

                System.out.printf("O Resultado da divisão: %.1f %n", resultado);
            }
            else {
                System.out.println("Divisão impossivel!!");

            }

            System.out.println("=".repeat(30));
        }
    }
}