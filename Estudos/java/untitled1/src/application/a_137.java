package application;

import application.entities.Conta;
import application.entities.ContaEmpresarial;
import application.entities.ContasSalvas;

public class a_137 {
    public static void main(String[] args) {
        Conta conta = new Conta(1001, "Alex", 0.0);
        ContaEmpresarial ceConta = new ContaEmpresarial(1002, "Maria", 0.0, 500.0);

        //UPCASTING

        Conta conta1 = ceConta;
        Conta conta2 = new ContaEmpresarial(1003, "Bob", 0.0, 200.0);
        Conta conta3 = new ContasSalvas(1004, "Anna", 0.0, 0.01);

        //Dowcasting
        ContaEmpresarial conta4 = (ContaEmpresarial) conta2;
        conta4.emprestimo(100.0);

        if (conta3 instanceof ContaEmpresarial){
            ContaEmpresarial conta5 = (ContaEmpresarial) conta3;
            conta5.emprestimo(200.0);
            System.out.print("Empréstimo");
        }
        if (conta3 instanceof ContasSalvas){
            ContasSalvas conta5 = (ContasSalvas) conta3;
            conta5.atualizarSaldo();
            System.out.print("Atualizado!");
        }
    }
}
