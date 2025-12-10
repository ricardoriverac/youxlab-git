package application;

import java.util.Locale;
import java.util.Scanner;

public class a_96_ex9 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        System.out.print("Caro usuário, por favor insira quantos alunos serão cadastrados: ");
        int quantidadeAlunos = sc.nextInt();
        String[] nome = new String[quantidadeAlunos];
        double[] nota1 = new double[quantidadeAlunos];
        double[] nota2 = new double[quantidadeAlunos];

        for (int i = 0; i < quantidadeAlunos; i++) {
            sc.nextLine();
            System.out.printf("Caro usuário, digite o nome do %do aluno(a) ", i+1);
            nome[i] = sc.nextLine();
            System.out.printf("Caro usuário, digite a nota do primeiro semestre do aluno(a) %s ", nome[i]);
            nota1[i] = sc.nextDouble();
            System.out.printf("Caro usuário, digite a nota do segundo semestre do aluno(a) %s ", nome[i]);
            nota2[i] = sc.nextDouble();
        }
        System.out.print("Alunos aprovados: ");
        for (int i = 0; i < quantidadeAlunos; i++) {
            if((nota1[i] + nota2[i]) / 2 >= 6.0){
                System.out.println(nome[i]);
            }
        }
    }
}
