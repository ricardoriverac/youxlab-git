package curso_completo_java.sessao_17.exercicios.exercicio02.application;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class program {

        public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);

            Set<Integer> alunos = new HashSet<>();

            System.out.print("Quantos alunos tem no curso A?: ");
            int alunosA = sc.nextInt();
            for (int i = 0; i < alunosA; i++) {
                alunos.add(sc.nextInt());
            }

            System.out.print("Quantos alunos tem no curso B?: ");
            int alunosB = sc.nextInt();
            for (int i = 0; i < alunosB; i++) {
                alunos.add(sc.nextInt());
            }

            System.out.print("Quantos alunos tem no curso C?: ");
            int alunosC = sc.nextInt();
            for (int i = 0; i < alunosC; i++) {
                alunos.add(sc.nextInt());
            }

            System.out.println("Total de alunos do instrutor Alex: " + alunos.size());
        }
    }


