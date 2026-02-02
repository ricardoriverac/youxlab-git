package curso_completo_java.sessao_05.exercicios;

/* Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode
começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.*/

import java.util.Scanner;


public class exercicio_iniciante04 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);


        System.out.println("Qual a hora ínicial do jogo?: ");
        int inicio = sc.nextInt();

        System.out.println("Qual a hora final do jogo?: ");
        int fim = sc.nextInt();

        int duracao;

        if (inicio < fim) {
            duracao = inicio - fim;
        }
        else {
            duracao = 24 - inicio + fim;
        }

        System.out.println("O jogo durou " + duracao + " horas");

        sc.close();
    }

    }
