package secao_13.metodosAbstratos.exerciciofixa.programaprincipal;

import secao_13.metodosAbstratos.exerciciofixa.entities.Company;
import secao_13.metodosAbstratos.exerciciofixa.entities.Individual;
import secao_13.metodosAbstratos.exerciciofixa.entities.TaxPayer;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class TaxProgram {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        List<TaxPayer> list = new ArrayList<>();

        System.out.println("Enter the number of tax payers: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.println("Tax payer #" + (i + 1) + " data:");
            System.out.print("Individual or company (i/c)? ");
            char ch = sc.next().charAt(0);
            System.out.print("Name: ");
            sc.next();
            String name = sc.nextLine();
            System.out.print("Anual income: ");
            double income = sc.nextDouble();

            if (ch == 'i'){
                System.out.print("Health expenditures: ");
                double health = sc.nextDouble();
                list.add(new Individual(name, income, health));
            }else {
                System.out.print("Number of employees: ");
                int emp = sc.nextInt();
                list.add(new Company(name, income, emp));
            }


            double sum = 0.0;
            System.out.println();
            System.out.println("TAXES PAID:");


            for (TaxPayer tp : list) {
                double tax = tp.tax();
                System.out.println(tp.getName() + ": $ " + String.format("%.2f", tax));
                sum += tax;
            }

            System.out.println();
            System.out.println("TOTAL TAXES: $ " + String.format("%.2f", sum));

            sc.close();
        }
    }
}
