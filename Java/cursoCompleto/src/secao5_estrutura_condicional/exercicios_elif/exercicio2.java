package secao5_estrutura_condicional.exercicios_elif;

import java.util.Scanner;

public class exercicio2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int lendo;
        System.out.println("Digite um número: ");
        lendo = sc.nextInt();
        if (lendo % 2 == 0) {
            System.out.println("PAR");
        }
        else {
            System.out.println("ÍMPAR");
        }
    }
}
