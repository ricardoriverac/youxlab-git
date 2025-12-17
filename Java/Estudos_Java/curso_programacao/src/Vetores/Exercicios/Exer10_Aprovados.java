package Vetores.Exercicios;

import java.util.Locale;
import java.util.Scanner;

public class Exer10_Aprovados {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        System.out.print("Quantos alunos serão digitados: ");
        int qntAlunos = sc.nextInt();
        String[] nomeAlunos = new String[qntAlunos];
        double[] nota1Aluno = new double[qntAlunos];
        double[] nota2Aluno = new double[qntAlunos];

        for (int i = 0; i < qntAlunos; i++) {
            System.out.println("Digite nome, primeira e segunda nota do " + (i+1) + "o aluno:");
            nomeAlunos[i] = sc.next();
            nota1Aluno[i] = sc.nextDouble();
            nota2Aluno[i] = sc.nextDouble();
        }

        double somaNotas = 0;
        double mediaNotas = 0;
        String alunosAprovados = "";

        for (int i = 0; i < qntAlunos; i++) {
            somaNotas = nota1Aluno[i] + nota2Aluno[i];
            mediaNotas = somaNotas / 2;
            if (mediaNotas >= 6.0) {
                alunosAprovados += nomeAlunos[i] + "\n";
            }
        }
        System.out.println("ALUNOS APROVADOS: \n" + alunosAprovados);




        sc.close();
    }
}
