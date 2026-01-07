package application;

import application.entities.Conta;
import application.entities.ContasSalvas;

public class a_140 {
    public static void main(String[] args) {

        Conta x = new Conta(1020, "Alex", 1000.0);
        Conta y = new ContasSalvas(1023, "Maria", 1000.0, 0.01);
        x.saque(50.0);
        y.saque(50.0);

        System.out.println(x.getSaldo());
        System.out.println(y.getSaldo());
    }
}
