package curso_completo_java.sessao_13.pratica.exemplo_pratica02.application;


import curso_completo_java.sessao_13.pratica.exemplo_pratica02.entities.Account;
import curso_completo_java.sessao_13.pratica.exemplo_pratica02.entities.BusinessAccount;

public class program {

    public static void main(String[] args) {

        Account acc = new Account(1001, "Alex", 0.0);
        BusinessAccount bacc = new BusinessAccount(1002, "Maria", 0.0, 500.0);

        // UPCASTING

        Account acc1 = bacc;
        Account acc2 = new BusinessAccount(1003, "Bob", 0.0, 200.0);


    }
}
