package Estrutura_Condicional.aula_01;

import java.util.Scanner;

public class exer7 {
    static void main() {
        Scanner sc = new Scanner(System.in);

        double x, y;
        System.out.println("Digite o eixo X:");
        x = sc.nextDouble();
        System.out.println("Digite o eixo Y:");
        y = sc.nextDouble();

        if (x == 0 && y == 0) {
            System.out.println("Origem");
        }
        else if (x == 0 && y != 0) {
            System.out.println("Eixo X");
        }
        else if (y == 0 && x != 0) {
            System.out.println("Eixo Y");
        }
        else if (x > 0 && y > 0) {
            System.out.println("Q1");
        }
        else if (x < 0 && y > 0) {
            System.out.println("Q2");
        }
        else if (x < 0 && y < 0) {
            System.out.println("Q3");
        }
        else if (y < 0 && x > 0) {
            System.out.println("Q4");
        }
    }
}
