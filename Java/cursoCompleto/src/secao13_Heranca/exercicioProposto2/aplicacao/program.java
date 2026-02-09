package secao13_Heranca.exercicioProposto2.aplicacao;

import secao13_Heranca.exercicioProposto2.entities.PessoaFisica;
import secao13_Heranca.exercicioProposto2.entities.PessoaJuridica;
import secao13_Heranca.exercicioProposto2.entities.TaxPayer;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class program {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        List<TaxPayer> taxPayers = new ArrayList<>();

        System.out.print("Enter the number of tax payers: ");
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("Individual or Company? (C/I) ");
            char condi = sc.next().toUpperCase().charAt(0);
            System.out.print("Name: ");
            String name = sc.next();
            System.out.print("\nAnual Income: ");
            Double anualIncome = sc.nextDouble();
            if (condi == 'I') {

                System.out.print("Healthy expenditures: ");
                Double healtyExpenditures = sc.nextDouble();
                taxPayers.add(new PessoaFisica(name, anualIncome, healtyExpenditures));
            }
            else {
                System.out.print("Number of employees: ");
                int employees = sc.nextInt();
                taxPayers.add(new PessoaJuridica(name, anualIncome, employees));
            }

        }
        System.out.println("TAXES PAID: ");
        double sum = 0;
        double taxes = 0;
        for(TaxPayer payer : taxPayers){
            taxes = payer.tax();
            sum += taxes;
            System.out.print("\n" + payer.getName() + ": $" + payer.tax());
        }
        System.out.println("\nTOTAL TAXES: $" + sum);
        sc.close();

    }
}
