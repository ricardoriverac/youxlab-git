package application;

import application.entities.Conta;
import application.entities.ContaEmpresarial;
import application.entities.ContasSalvas;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class a_143 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        List<Conta> contas = new ArrayList<>();

        contas.add(new ContasSalvas(1001, "Alex", 500.0, 0.01));
        contas.add(new ContaEmpresarial(1002, "Maria", 1000.0, 400.0));
        contas.add(new ContasSalvas(1004, "Bob", 300.0, 0.01));
        contas.add(new ContaEmpresarial(1005, "Anna", 500.0, 500.0));

        double sum = 0.0;
        for (Conta c : contas){
            sum+= c.getSaldo();
        }
        System.out.printf("Renda total: %.2f%n", sum);

    }
}
