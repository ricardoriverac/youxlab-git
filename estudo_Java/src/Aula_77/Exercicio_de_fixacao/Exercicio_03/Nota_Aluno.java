package Aula_77.Exercicio_de_fixacao.Exercicio_03;

import java.util.Locale;
import java.util.Scanner;

public class Nota_Aluno {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Class_notaAluno notaAluno = new Class_notaAluno();

        System.out.print("Digite a 1º nota: ");
        notaAluno.nota1 = sc.nextDouble();

        System.out.print("Digite a 2º nota: ");
        notaAluno.nota2 = sc.nextDouble();

        System.out.print("Digite a 3º nota: ");
        notaAluno.nota3 = sc.nextDouble();

        System.out.printf("Sua nota final é = %.2f", notaAluno.somatorioNotas());
        System.out.println(notaAluno.verificador());
    }
}
