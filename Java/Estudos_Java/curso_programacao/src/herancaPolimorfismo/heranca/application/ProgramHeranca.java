package herancaPolimorfismo.heranca.application;

import herancaPolimorfismo.heranca.entities.BusinessAccount;

public class ProgramHeranca {

    static void main() {

        BusinessAccount account = new BusinessAccount(8010, "Bob Brown", 0.0, 500.0);
        System.out.println(account.getBalance());
    }
}
