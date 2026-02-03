package Secao_16.Exercicio_01.application;

import Secao_16.Exercicio_01.model.entities.Contract;
import Secao_16.Exercicio_01.model.entities.Installment;
import Secao_16.Exercicio_01.model.services.ContractService;
import Secao_16.Exercicio_01.model.services.PaypalService;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        System.out.println("Enter the contract's data:");
        System.out.print("Number: ");
        int number = sc.nextInt();
        sc.nextLine();
        System.out.print("Date (dd/MM/yyyy): ");
        LocalDate date = LocalDate.parse(sc.nextLine(), dtf);
        System.out.print("Contract value: ");
        double price = sc.nextDouble();
        System.out.print("Number of installments: ");
        int installments = sc.nextInt();

        Contract contract = new Contract(number, date, price);
        ContractService cs = new ContractService(new PaypalService());
        cs.processContract(contract, installments);

        System.out.println("Receipt");
        for (Installment i : contract.getInstallments()) {
            System.out.println(i);
        }
        sc.close();
    }
}
