package Estruturas_respectivas06.exercicios;

import java.util.Scanner;

public class exercicio_iniciante10 {

        public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);

            System.out.println("Digite um valor:");
            int valor = sc.nextInt();

            for (int i=1; i<=valor; i++) {

                int primeiro = i;
                int segundo = i * i;
                int terceiro = i * i * i;
                System.out.printf("%d %d %d%n", primeiro, segundo, terceiro);
            }

            sc.close();
        }
    }

