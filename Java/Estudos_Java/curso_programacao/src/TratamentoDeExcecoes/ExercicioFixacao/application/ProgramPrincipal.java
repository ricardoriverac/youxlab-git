package TratamentoDeExcecoes.ExercicioFixacao.application;

import TratamentoDeExcecoes.ExercicioFixacao.model.entities.Account;
import TratamentoDeExcecoes.ExercicioFixacao.model.exceptions.WithDrawAccount;

import java.util.InputMismatchException;
import java.util.Locale;
import java.util.Scanner;

public class ProgramPrincipal {

    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        try {
            System.out.println("Enter account data: ");
            System.out.print("Number: ");
            int numberAccount = sc.nextInt();
            System.out.print("Holder: ");
            sc.nextLine();
            String holder = sc.nextLine();
            System.out.print("Initial balance: ");
            double initialBalance = sc.nextDouble();
            System.out.print("withdraw Limit: ");
            double withdraw = sc.nextDouble();

            Account account = new Account(numberAccount, holder, initialBalance, withdraw);

            System.out.println();
            System.out.print("Enter amount for withdraw: ");
            double amountWithdraw = sc.nextDouble();

            account.withdraw(amountWithdraw);
            System.out.println("New balance: " + String.format("%.2f", account.getBalance()));

        }

        catch (WithDrawAccount w){
            System.out.println("Withdraw error: " + w.getMessage());
        }
        catch (RuntimeException e){
            System.out.println("Unexpected error!");
        }

        sc.close();
    }
}
