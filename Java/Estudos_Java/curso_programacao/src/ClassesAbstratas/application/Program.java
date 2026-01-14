package ClassesAbstratas.application;

import ClassesAbstratas.entities.Account;
import ClassesAbstratas.entities.BusinessAccount;
import ClassesAbstratas.entities.SavingsAccount;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Program {
    static void main() {

        Locale.setDefault(Locale.US);

        List<Account> accounts = new ArrayList<>();

        accounts.add(new SavingsAccount(1001, "Alex", 500.0, 0.01));
        accounts.add(new BusinessAccount(1001, "Maria", 1000.0, 400.0));
        accounts.add(new SavingsAccount(1004, "Bob", 300.0, 0.01));
        accounts.add(new BusinessAccount(1005, "Anna", 500.0, 500.0));

        double soma = 0.0;
        for (Account acc : accounts){
            soma += acc.getBalance();
        }

        System.out.printf("TOTAL BALANCE: %.2f%n", soma);

        for (Account acc : accounts){
            acc.deposit(10.0);
        }

        for (Account acc : accounts) {
            System.out.printf("Update balance for account %d: %.2f%n", acc.getNumber(), acc.getBalance());
        }
    }
}
