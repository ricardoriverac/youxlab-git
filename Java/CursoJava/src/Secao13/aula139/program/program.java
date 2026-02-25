package Secao13.aula139.program;

import Secao13.aula139.entities.Account2;
import Secao13.aula139.entities.BusinessAccount2;
import Secao13.aula139.entities.SavingsAccount2;

public class program {
    public static void main(String[] args) {

        Account2 acc1 = new Account2(1001, "Alex", 1000.0);
        acc1.withdraw(200.0);
        System.out.println(acc1.getBalance());

        Account2 acc2 = new SavingsAccount2(1002, "Maria", 1000.0, 0.01);
        acc2.withdraw(200.0);
        System.out.println(acc2.getBalance());

        Account2 acc3 = new BusinessAccount2(1003, "Bob", 1000.0, 500.0);
        acc3.withdraw(200.0);
        System.out.println(acc3.getBalance());
    }
}
