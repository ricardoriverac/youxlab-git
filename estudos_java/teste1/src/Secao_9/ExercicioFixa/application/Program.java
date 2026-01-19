package Secao_9.ExercicioFixa.application;

import Secao_9.ExercicioFixa.entities.Account;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Account acc = new Account();

        double value;
        System.out.print("Enter account number: ");
        int accNumber = sc.nextInt();
        acc.setAccNumber(accNumber);

        System.out.print("Enter account holder: ");
        sc.nextLine();
        String name = sc.nextLine();
        acc.setName(name);

        System.out.print("Is there an initial deposit (y/n)?");
        String answer = sc.next();

        if ( answer.charAt(0) == 'y' ) {
            System.out.print("Enter initial deposit value: ");
            value = sc.nextDouble();
            acc.deposit(value);
        }

        System.out.println();
        System.out.println("Account data:");
        System.out.println(acc);
        System.out.println();

        System.out.print("Enter a deposit value: ");
        value = sc.nextDouble();
        acc.deposit(value);

        System.out.println("Updated account data:");
        System.out.println(acc);
        System.out.println();

        System.out.print("Enter a withdraw value: ");
        value = sc.nextDouble();
        acc.withdraw(value);

        System.out.println("Updated account data:");
        System.out.println(acc);
    }
}
