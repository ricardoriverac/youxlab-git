package Secao_14.Aula_158.Exercicio_Fixacao.applications;

import Secao_14.Aula_158.Exercicio_Fixacao.entities.Account;
import Secao_14.Aula_158.Exercicio_Fixacao.exceptions.SaqueInvalidoExceptions;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        try {
            System.out.println("Enter account data");

            System.out.print("Number: ");
            int number = sc.nextInt();

            System.out.print("Holder: ");
            sc.nextLine();
            String holder = sc.nextLine();

            System.out.print("Initial balance: ");
            double balnceInitial = sc.nextDouble();

            System.out.print("Withdraw limit: ");
            double withdrawLimit = sc.nextDouble();

            Account acc = new Account(number, holder, withdrawLimit);
            acc.deposit(balnceInitial);

            System.out.print("\nEnter amount for withdraw: ");
            acc.withdraw(sc.nextDouble());

            System.out.println(acc);
        }
        catch (SaqueInvalidoExceptions e) {
            System.out.println("Withdraw error: " + e.getMessage());
        }
    }
}
