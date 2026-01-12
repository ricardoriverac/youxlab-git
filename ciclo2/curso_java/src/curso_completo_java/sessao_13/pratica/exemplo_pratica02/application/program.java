package curso_completo_java.sessao_13.pratica.exemplo_pratica02.application;

// AULA 137 - Upcasting e downcasting

import curso_completo_java.sessao_13.pratica.exemplo_pratica02.entities.Account;
import curso_completo_java.sessao_13.pratica.exemplo_pratica02.entities.BusinessAccount;
import curso_completo_java.sessao_13.pratica.exemplo_pratica02.entities.SavingsAccount;

public class program {

    public static void main(String[] args) {

        Account acc = new Account(1001, "Alex", 0.0);
        BusinessAccount bacc = new BusinessAccount(1002, "Maria", 0.0, 500.0);

        // UPCASTING

        Account acc1 = bacc;
        Account acc2 = new BusinessAccount(1003, "Bob", 0.0, 200.0);
        Account acc3 = new SavingsAccount(100, "Anna", 0.0, 0.01);

        //  DOWNCASTING

        BusinessAccount acc4 = (BusinessAccount) acc2;
        acc4.loan(100.0);

        // BusinessAccount acc5 = (BusinessAccount) acc3;


        if (acc3 instanceof BusinessAccount) {
            BusinessAccount acc5 = (BusinessAccount) acc3;
            acc5.loan(200.0);
            System.out.println("Loan");
        }

        if (acc3 instanceof SavingsAccount) {
            SavingsAccount acc5 = (SavingsAccount) acc3;
            acc5.updateBalance();
            System.out.println("Update!");
        }


    }
}
