package curso_completo_java.sessao_06.exercicios;

/* Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema
cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo
menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).*/

import java.util.Scanner;

public class exercicio_iniciante02 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);


                System.out.println("Digite a primeira coodernada (x):");
                int x = sc.nextInt();

                System.out.println("Digite a segunda coodernada (y):");
                int y = sc.nextInt();

                while (x != 0 && y != 0) {
                    if (x > 0 && y > 0) {
                        System.out.println("primeiro\n");
                    }
                    else if (x < 0 && y > 0) {
                        System.out.println("segundo\n");
                    }
                    else if (x < 0 && y < 0) {
                        System.out.println("terceiro\n");
                    }
                    else {
                        System.out.println("quarto\n");
                    }
                    System.out.println("Digite outra coordenada (x):");
                    x = sc.nextInt();
                    System.out.println("Digite outra coordenada (y):");
                    y = sc.nextInt();
                }
                System.out.println("Sua cordenada tem valor nula! Encerrado.");
                sc.close();
            }
        }