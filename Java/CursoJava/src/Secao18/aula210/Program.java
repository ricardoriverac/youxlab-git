package Secao18.aula210;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<Employee> employees = new ArrayList<>();
        System.out.print("Enter full file path: ");
        String path = sc.nextLine();
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {

            String line = br.readLine();
            while (line != null) {
                String[] fields = line.split(",");
                String name = fields[0];
                String email = fields[1];
                Double salary = Double.parseDouble(fields[2]);
                employees.add(new Employee(name, email, salary));
                line = br.readLine();
            }

            System.out.print("Enter salary: ");
            double salaryLimit = sc.nextDouble();

            System.out.println("\nEmail of people whose salary is more than " + String.format("%.2f", salaryLimit) + ":");
            List<String> emails = employees.stream()
                    .filter(e -> e.getSalary() > salaryLimit)
                    .map(Employee::getEmail)
                    .sorted()
                    .collect(Collectors.toList());
            emails.forEach(System.out::println);

            double sum = employees.stream()
                    .filter(e -> e.getName().startsWith("M"))
                    .mapToDouble(Employee::getSalary)
                    .sum();
            System.out.println("\nSum of salary of people whose name starts with 'M': " + String.format("%.2f", sum));

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }

        sc.close();
    }
}

