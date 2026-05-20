package Estrutura_Condicional.aula_01;

import java.util.Scanner;

public class exer5 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int codigo, quantidade;
        double preco;

        System.out.println("Código do produto:");
        codigo = sc.nextInt();
        System.out.println("Quantidade:");
        quantidade = sc.nextInt();

        if (codigo == 1) {
            preco = 4.0;
            preco *= quantidade;
        }
        else if (codigo == 2) {
            preco = 4.5;
            preco *= quantidade;
        }
        else if (codigo == 3) {
            preco = 5.0;
            preco *= quantidade;
        }
        else if (codigo == 4) {
            preco = 2.0;
            preco *= quantidade;
        }
        else {
            preco = 1.5;
            preco *= quantidade;
        }
        System.out.println("Total = " + preco);
    }
}
