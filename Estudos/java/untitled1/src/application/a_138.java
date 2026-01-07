package application;

import application.entities.Conta;
import application.entities.ContaEmpresarial;
import application.entities.ContasSalvas;

public class a_138 {
    public static void main(String[] args) {

        Conta conta1 = new Conta(1001, "Alex", 1000.0);
        conta1.saque(200.0);
        System.out.println(conta1.getSaldo());

        Conta conta2 = new ContasSalvas(1002, "Maria", 1000.0, 0.01);
        conta2.saque(conta2.getSaldo());

        Conta conta3 = new ContaEmpresarial(1003, "Bob", 1000.0, 500.0);
        conta3.saque(200.0);
        System.out.println(conta3.getSaldo());
    }
}
