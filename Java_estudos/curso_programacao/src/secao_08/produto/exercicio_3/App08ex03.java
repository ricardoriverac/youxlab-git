package secao_08.produto.exercicio_3;

import java.util.Locale;
import java.util.Scanner;

public class App08ex03 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Student stu = new Student();

        System.out.print("Nome: ");
        stu.name = sc.nextLine();
        System.out.print("Primeiro Trimestre: ");
        stu.nota1 = sc.nextDouble();
        System.out.print("Segundo Trimestre: ");
        stu.nota2 = sc.nextDouble();
        System.out.print("Terceiro Trimestre: ");
        stu.nota3 = sc.nextDouble();
        double notaFinal1 = stu.nota1 + stu.nota2 + stu.nota3;

        System.out.printf("FINAL GRADE = %.2f%n", notaFinal1);
        if (stu.boletim(notaFinal1) > 60) {
            System.out.println("PASS");
        } else {
            System.out.println("FAILED");
            System.out.printf("MISSING %.2f POINTS", stu.boletim(notaFinal1));
        }
    }
}