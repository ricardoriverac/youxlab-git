package herancaPolimorfismo.Exercicios.ExercicioResolvido.application;

import herancaPolimorfismo.Exercicios.ExercicioResolvido.entities.Employee;
import herancaPolimorfismo.Exercicios.ExercicioResolvido.entities.OutsourcedEmployee;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Program {
    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        List<Employee> employees = new ArrayList<>();

        System.out.print("Enter the number of employees: ");
        int qntEmployees = sc.nextInt();
        for (int i = 0; i < qntEmployees; i++) {
            System.out.println("Employee #" + (i+1) + " data:");
            System.out.print("Outsourced (y/n)? ");
            char outSourced = sc.next().toLowerCase().charAt(0);
            System.out.print("Name: ");
            String employeeName = sc.next();
            System.out.print("Hours: ");
            int hours = sc.nextInt();
            System.out.print("Value per hour: ");
            double valuePerHour = sc.nextDouble();

            if (outSourced == 'y'){
                System.out.print("Additional charge: ");
                double additionalCharge = sc.nextDouble();
                employees.add(new OutsourcedEmployee(employeeName, hours, valuePerHour, additionalCharge));
            }
            else {
                employees.add(new Employee(employeeName, hours, valuePerHour));
            }

        }
        System.out.println("PAYMENTS:");
        for (Employee emp : employees) {
            System.out.println(emp.getName() + " - $ " + String.format("%.2f", emp.payment()));
        }


        sc.close();
    }
}
