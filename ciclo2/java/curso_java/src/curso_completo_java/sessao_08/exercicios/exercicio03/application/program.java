package curso_completo_java.sessao_08.exercicios.exercicio03.application;

import curso_completo_java.sessao_08.exercicios.exercicio03.entities.Student;

import java.util.Locale;
import java.util.Scanner;;

public class program {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Student student = new Student();

        System.out.println("Digite seu nome");
        student.name = sc.nextLine();

        System.out.println("Digite sua 1ª nota: ");
        student.grade1 = sc.nextDouble();
        System.out.println("Digite sua 2ª nota: ");
        student.grade2 = sc.nextDouble();
        System.out.println("Digite sua 3ª nota: ");
        student.grade3 = sc.nextDouble();

        System.out.printf("FINAL GRADE: %.2f%n", student.finalGrade());

        if (student.finalGrade() < 60.0) {
            System.out.println("FAILED");
            System.out.printf("MISSING %.2f POINTS%n", student.missingPoints());
        } else {
            System.out.println("PASS");
        }

        sc.close();

    }
}
