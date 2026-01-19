package Secao_8.Exercicio_2.Program;

import Secao_8.Exercicio_2.Data.Employee;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        Employee employee = new Employee();
        System.out.print("Name: ");
        String name = sc.nextLine();
        employee.name = name;
        System.out.print("Gross salary: ");
        double grossSalary = sc.nextDouble();
        employee.grossSalary = grossSalary;
        System.out.print("Tax: ");
        double tax = sc.nextDouble();
        employee.tax = tax;

        System.out.printf("Employee: %s, $ %.2f%n", employee.name, employee.NetSalary());

        System.out.print("Which percentage to increase salary? ");
        double percentage = sc.nextDouble();
        employee.IncreaseSalary(percentage);
        System.out.println(employee.toString());
    }
}
