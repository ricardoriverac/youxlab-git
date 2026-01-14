package MetodosAbstratos.ExercicioFixacaoAbstratos.application;

import MetodosAbstratos.ExercicioFixacaoAbstratos.entities.Company;
import MetodosAbstratos.ExercicioFixacaoAbstratos.entities.Individual;
import MetodosAbstratos.ExercicioFixacaoAbstratos.entities.TaxPayer;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class ProgramPrincipal {
    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of tax payers: ");
        int numberOfEmployee = sc.nextInt();

        List<TaxPayer> taxPayers = new ArrayList<>();

        for (int i = 0; i < numberOfEmployee; i++) {
            System.out.print("Tax payer #" + (i+1) + " data:");
            System.out.print("Individual or company (i/c)? ");
            char ic = sc.next().toLowerCase().charAt(0);
            System.out.print("Name: ");
            sc.nextLine();
            String name = sc.nextLine();
            System.out.print("Anual income: ");
            double anualIncome = sc.nextDouble();

            if (ic == 'i'){
                System.out.print("Health expenditures: ");
                double healthExpenditures = sc.nextDouble();
                taxPayers.add(new Individual(name, anualIncome, healthExpenditures));
            }

            else if (ic == 'c'){
                System.out.print("Number of employees: ");
                int numberEmployees = sc.nextInt();
                taxPayers.add(new Company(name, anualIncome, numberEmployees));
            }
        }

        System.out.println();
        System.out.println("TAXES PAID:");
        for (TaxPayer tp : taxPayers){
            System.out.print(tp.getName() + ": $ " + String.format("%.2f%n", tp.tax()));
        }

        double totalTaxes = 0.0;
        for (TaxPayer tp : taxPayers){
            totalTaxes += tp.tax();
        }
        System.out.println();
        System.out.print("TOTAL TAXES: " + String.format("%.2f%n", totalTaxes));


        sc.close();

    }
}
