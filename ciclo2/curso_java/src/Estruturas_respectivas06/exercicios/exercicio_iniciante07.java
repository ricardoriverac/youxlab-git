package Estruturas_respectivas06.exercicios;

/* Fazer um programa para ler um número N. Depois leia N pares de números e mostre a divisão do primeiro pelo
segundo. Se o denominador for igual a zero, mostrar a mensagem "divisao impossivel"*/

import java.util.Scanner;

public class exercicio_iniciante07 {

    public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);

        System.out.println("Digite um valor: ");
            int n = sc.nextInt();

            for (int i=0; i<n; i++) {

                System.out.println("Digite outro valor");
                int x = sc.nextInt();
                System.out.println("Digite outro: ");
                int y = sc.nextInt();

                if (y == 0) {
                    System.out.println("divisao impossivel");
                }
                else {
                    double div = (double) x / y;
                    System.out.printf("%.1f%n", div);
                }
            }

            sc.close();
        }
    }

