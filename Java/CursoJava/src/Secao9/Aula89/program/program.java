package Secao9.Aula89.program;

import Secao9.Aula89.utiliz.conta;

import java.util.Locale;
import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        conta Conta = new conta();
        System.out.print("Enter account number: ");
        int number = sc.nextInt();
        System.out.print("Enter account holder: ");
        sc.nextLine();
        String holder = sc.nextLine();
        System.out.print("Is there na initial deposit (y/n)? ");
        char response = sc.nextLine().charAt(0);
        if (response == 'y') {
            System.out.print("Enter initial deposit value: ");
            double valorinicial = sc.nextDouble();
            Conta = new conta(number,holder,valorinicial);
        }
        else {
            Conta= new conta(number, holder);
        }
        System.out.println();
        System.out.print("Account data: \n");
        System.out.print(Conta);
        System.out.println();

        System.out.println();
        System.out.print("Enter a deposit value: ");
        double depositValor = sc.nextDouble();
        Conta.deposito(depositValor);
        System.out.println("Updated account data: ");
        System.out.print(Conta);
        System.out.println();

        System.out.println();
        System.out.print("Enter a whitdraw value: ");
        double whitdrawvalor = sc.nextDouble();
        Conta.saque(whitdrawvalor);

        System.out.println("Updated account data: ");
        System.out.print(Conta);

    sc.close();
    }
}
