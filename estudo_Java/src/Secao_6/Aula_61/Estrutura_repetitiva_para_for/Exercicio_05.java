package Aula_61.Estrutura_repetitiva_para_for;

import java.util.Scanner;

public class Exercicio_05 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int Valor_fatorial, fatorial = 1;

        System.out.print("Digite um valor: ");
        Valor_fatorial = sc.nextInt();

        for (int i = Valor_fatorial; i >= 1; i--) {

            fatorial = fatorial * i;

            if (i != Valor_fatorial) {
                System.out.print(" * ");
            }
            System.out.print( i);
        }

        System.out.print(" = " + fatorial);
    }
}