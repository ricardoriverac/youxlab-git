package Secao_8.Exercicio_3.entities;

import Secao_8.Exercicio_3.application.Student;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        Student student = new Student();
        System.out.println("Enter the student name and grades:");
        String name = sc.nextLine();
        student.firstGrade = sc.nextDouble();
        student.secondGrade = sc.nextDouble();
        student.thirdGrade = sc.nextDouble();
        double grade = student.finalGrade();
        System.out.println("NAME = " + name);
        student.result(grade);
    }
}
