package Secao10.aula107;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class programa {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<codigo> list = new ArrayList<>();

        System.out.print("How many employees will be registered? ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {

            System.out.println("Employee #" + i + ": ");
            System.out.print("Id: ");
            int id = sc.nextInt();
            sc.nextLine();

            System.out.print("Name: ");
            String name = sc.nextLine();

            System.out.print("Salary: ");
            double salary = sc.nextDouble();

            list.add(new codigo(id, name, salary));
        }

        System.out.print("Enter the employee id that will have salary increase: ");
        int idSalary = sc.nextInt();

        codigo emp = null;

        for (codigo e : list) {
            if (e.getId() == idSalary) {
                emp = e;
                break;
            }
        }

        if (emp == null) {
            System.out.println("This id does not exist!");
        } else {
            System.out.print("Enter the percentage: ");
            double percentage = sc.nextDouble();
            emp.increaseSalary(percentage);
        }

        System.out.println();
        System.out.println("List of employees:");
        for (codigo e : list) {
            System.out.println(e);
        }

        sc.close();
    }
}

