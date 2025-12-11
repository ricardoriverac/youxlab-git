package secao_08.produto.exercicio_2;

import secao_08.produto.exercicio_2.entities.Employee;

import java.util.Locale;
import java.util.Scanner;

public class App08ex02 {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        Employee emp = new Employee();
        double percent;

        System.out.println("Name:");
        emp.name = sc.nextLine();
        System.out.println("Gross Salary: ");
        emp.grossSalary = sc.nextDouble();
        System.out.println("Tax: ");
        emp.tax = sc.nextDouble();
        System.out.println(emp.toString());
        System.out.println("Which percentage to increase salary? ");
        percent = sc.nextDouble();
        emp.increaseSalary(percent);
        System.out.println("Updated data:\n" + emp.toString());

    }
}
