package Secao_10.ExercicioProposto.application;

import Secao_10.ExercicioProposto.entities.Employee;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("How many employees will be registered? ");
        int quantity = sc.nextInt();
        List<Employee> employeeList = new ArrayList<>();

        for (int i=0 ; i<quantity ; i++) {

            System.out.println("Employee #"+ (i+1));
            System.out.print("Id: ");
            Integer id = sc.nextInt();
            System.out.print("Name: ");
            sc.nextLine();
            String name = sc.nextLine();
            System.out.print("Salary: ");
            Double salary = sc.nextDouble();
            System.out.println();
            Employee employee = new Employee(id, name, salary);
            employeeList.add(employee);
        }

        System.out.print("Enter the employee id that will have salary increase: ");
        int choice = sc.nextInt();

        //Employee existEmployee = employeeList.stream().filter(x -> x.id == choice).findFirst().orElse(null);

        boolean exist = false;

        for (Employee item : employeeList) {if (item.id == choice) {exist = true;break;}}

        if (!exist) {
            System.out.println("This id does not exist!");
        } else {
            for (Employee item : employeeList) {
                if (item.id == choice) {
                    System.out.print("Enter the percentage: ");
                    double percentage = sc.nextDouble();
                    item.setSalary(item.getSalary() * (1 + (percentage / 100)));
                }
            }
        }

        System.out.println("List of employees:");
        for (int i=0 ; i<quantity ; i++) {
            System.out.println(employeeList.get(i));
        }

        sc.close();
    }
}