package Programacao_Orientada_Objetos.EXERCICIO.application;

import Programacao_Orientada_Objetos.EXERCICIO.entities.BankAccount;

import java.util.Locale;
import java.util.Scanner;

public class Program {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        BankAccount bankAccount = new BankAccount();

        System.out.print("Enter account number: ");
        int number = sc.nextInt();
        bankAccount.setNumber(number);
        System.out.print("Enter account holder: ");
        String holder = sc.next();
        bankAccount.setHolder(holder);

        double deposit;
        char yN = 'y';
        System.out.print("Is there na initial deposit (y/n)? ");
        yN = sc.next().charAt(0);
        if (yN == 'y') {
            System.out.print("Enter initial deposit value: ");
            deposit = sc.nextDouble();
            bankAccount.deposit(deposit);
            System.out.println();
            System.out.println("Account data: ");
            System.out.printf("Account: %d, Holder: %s, Balance: $ %.2f", bankAccount.getNumber(), bankAccount.getHolder(), bankAccount.getBalance());
            System.out.println();
        }
        else {
            System.out.println();
            System.out.println("Account data: ");
            System.out.printf("Account %d, Holder: %s, Balance: $ %.2f", bankAccount.getNumber(), bankAccount.getHolder(), bankAccount.getBalance());
            System.out.println();
        }

        System.out.println();
        System.out.print("Enter a deposit value: ");
        deposit = sc.nextDouble();
        bankAccount.deposit(deposit);
        System.out.println("Updated account data: ");
        System.out.printf("Account %d, Holder: %s, Balance: $ %.2f", bankAccount.getNumber(), bankAccount.getHolder(), bankAccount.getBalance());

        System.out.println("\n");
        System.out.print("Enter a withdraw value: ");
        double remove = sc.nextDouble();
        bankAccount.WithDraw(remove);
        System.out.println("Updated account data:");
        System.out.printf("Account %d, Holder: %s, Balance: $ %.2f", bankAccount.getNumber(), bankAccount.getHolder(), bankAccount.getBalance());

        sc.close();
    }
}
