package Secao_12.Aula_130.Exercicio_resolvido1_Pt_1.Application;

import Secao_12.Aula_130.Exercicio_resolvido1_Pt_1.Entities.Department;
import Secao_12.Aula_130.Exercicio_resolvido1_Pt_1.Entities.HourContract;
import Secao_12.Aula_130.Exercicio_resolvido1_Pt_1.Entities.Worker;
import Secao_12.Aula_130.Exercicio_resolvido1_Pt_1.entities_enums.WorkerLevel;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) throws ParseException {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        System.out.print("Enter department's name: ");
        String departmentName = sc.nextLine();

        System.out.println("Enter worker data: ");

        System.out.print("Name: ");
        String workerName =  sc.nextLine();

        System.out.print("Level: ");
        String workerLevel = sc.nextLine();

        System.out.print("Base salary: ");
        double baseSalary = sc.nextDouble();

        Worker worker = new Worker(workerName, WorkerLevel.valueOf(workerLevel), baseSalary, new Department(departmentName));

        System.out.print("How many constracts to this worker? ");
        int n = sc.nextInt();

        for (int i=0; i<n; i++) {
            System.out.println("Enter contract #" + (i+1) + " data: ");

            System.out.print("Date (DD/MM/YYY): ");
            Date contractDate = sdf.parse(sc.next());

            System.out.print("Value per hour: ");
            double valuePerHour = sc.nextDouble();

            System.out.print("Duration hours: ");
            int hours = sc.nextInt();

            HourContract contract = new HourContract(contractDate, valuePerHour, hours);
            worker.addContract(contract);

        }
        System.out.println();
        System.out.print("Enter month and year to calculate income (MM/YYYY): ");

        String mothandyear = sc.next();
        int month = Integer.parseInt(mothandyear.substring(0,2));
        int year = Integer.parseInt(mothandyear.substring(3));

        System.out.println("Nome: " + worker.getName());
        System.out.println("Department: " + worker.getDepartment().getName());
        System.out.println("Income for " + mothandyear + ": " + String.format("%.2f", worker.income(year, month)));

        sc.close();
    }
}