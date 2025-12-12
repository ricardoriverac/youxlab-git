package Programacao_Orientada_Objetos.Exercicios.Employee;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Employee funcionario = new Employee();

        System.out.print("Name: ");
        funcionario.name = sc.nextLine();

        System.out.print("Gross salary: ");
        funcionario.grossSalary = sc.nextDouble();

        System.out.print("Tax: ");
        funcionario.tax = sc.nextDouble();

        System.out.println("Employee: " + funcionario.name + ", $ " + funcionario.netSalary());
        System.out.print("Which porcentage to increase salary? ");
        double porcent = sc.nextDouble();

        funcionario.increaseSalary(porcent);

        System.out.println("Updated data: " + funcionario.name + ", $ " + funcionario.netSalary());

        sc.close();
    }
}
