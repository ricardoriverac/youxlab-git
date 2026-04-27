package Secao_16.Aula_183.Default_Methods.application;

import Secao_16.Aula_183.Default_Methods.services.BrazilInterestService;
import Secao_16.Aula_183.Default_Methods.services.InterestService;
import Secao_16.Aula_183.Default_Methods.services.UsaInterestService;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Amount: ");
        double amount = sc.nextDouble();

        System.out.print("Months: ");
        int months = sc.nextInt();

        InterestService is = new BrazilInterestService(1.0);
        double payment = is.payment(amount, months);

        System.out.println("Paymen after " + months + " months:");
        System.out.println(String.format("%.2f", payment));

        sc.close();
    }
}