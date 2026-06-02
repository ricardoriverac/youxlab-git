package Secao_17.Aula_196.Exercicio_Fixacao.applications;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Set<Integer> set = new HashSet<>();
        String[] letras = {"A", "B", "C"};

        for (int i = 0; i <= 2; i++) {
            System.out.print("Quantos alunos para o curso " + letras[i] + "? ");
            int quantidadeAluno = sc.nextInt();

            for (int j = 1; j <= quantidadeAluno; j++) {
                set.add(sc.nextInt());
            }
        }

        System.out.println("Total de alunos: " + set.size());
    }
}
