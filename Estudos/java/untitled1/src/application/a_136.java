package application;

import application.entities.ContaEmpresarial;

public class a_136 {
    public static void main(String[] args) {

        ContaEmpresarial conta = new ContaEmpresarial(8010, "Bob Brown", 0.0, 500.0);

        System.out.println(conta.getSaldo());
    }
}
