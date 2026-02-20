package Aula_97.Vetores.Exercicio_Fixacao;

import java.util.Locale;
import java.util.Scanner;

public class Exercicio_10 {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos alunos serao digitados? ");
        int n = sc.nextInt();

        int c = 0;
        double nota1;
        double nota2;
        double media = 0;

        String[] vetorNomeAlunos = new String[n];
        String[] vetorNomeAprovados = new String[n];

        for (int i=0; i<n; i++) {
            c++;
            System.out.printf("Digite o nome, primeira e segunda nota do %d° aluno: %n", c);
            String o = sc.nextLine();
            vetorNomeAlunos[i] = sc.nextLine();
            nota1 = sc.nextDouble();
            nota2 = sc.nextDouble();

            media = (nota1 + nota2) / 2;

            if (media >= 6) {
                vetorNomeAprovados[i] = vetorNomeAlunos[i];
            }
        }

        System.out.println("Alunos aprovados: ");
        for (int i=0; i<n; i++) {
            if (vetorNomeAprovados[i] != null) {
                System.out.println(vetorNomeAprovados[i]);
            }
        }
    }
}
