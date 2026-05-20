package herancaPolimorfismo.UpcastingEDowncasting.application;

import herancaPolimorfismo.UpcastingEDowncasting.entities.Account;
import herancaPolimorfismo.UpcastingEDowncasting.entities.BusinessAccount;
import herancaPolimorfismo.UpcastingEDowncasting.entities.SavingsAccount;

public class Program {
    static void main() {
        Account acc = new Account(1001, "Luis", 0.0);
        BusinessAccount bacc = new BusinessAccount(1002, "Maria", 0.0, 500.0);

        // UPCASTING
        Account acc1 = bacc;
        Account acc2 = new BusinessAccount(1003, "Ágatha", 0.0, 200.0);
        Account acc3 = new SavingsAccount(1004, "Emily", 0.0, 0.01);

        // DOWNCASTING

        BusinessAccount acc4 = (BusinessAccount)acc2;
        acc4.loan(100.0);

        // BusinessAccount acc5 = (BusinessAccount)acc3; - NÃO PERIMTIDO, pois não é possivel dar downcasting na variavel acc3
        // que é do tipo SavingsAccount

        if (acc3 instanceof BusinessAccount) {
            BusinessAccount acc5 = (BusinessAccount)acc3;
            acc5.loan(200.0);
            System.out.println("Loan!");
        }

        if (acc3 instanceof SavingsAccount) {
            SavingsAccount acc5 = (SavingsAccount)acc3;
            acc5.updateBalance();
            System.out.println("Update!");
        }
    }
}
