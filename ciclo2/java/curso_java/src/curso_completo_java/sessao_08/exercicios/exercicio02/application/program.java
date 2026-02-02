package curso_completo_java.sessao_08.exercicios.exercicio02.application;

import curso_completo_java.sessao_08.exercicios.exercicio02.entities.Employee;

import java.util.Locale;
import java.util.Scanner;

public class program {

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Employee emp = new Employee();

        System.out.print("Name: ");
        emp.name = sc.nextLine();

        System.out.print("Gross salary: ");
        emp.grossSalary = sc.nextDouble();

        System.out.print("Tax: ");
        emp.tax = sc.nextDouble();

        System.out.println("Employee: \n" + emp);
        System.out.print("Which percentage to increase salary? \n");

        double percentage = sc.nextDouble();
        emp.increaseSalary(percentage);

        System.out.println("Updated data: \n" + emp);

        sc.close();

    }

}
