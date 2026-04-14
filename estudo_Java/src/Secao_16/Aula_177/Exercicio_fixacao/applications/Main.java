package Secao_16.Aula_177.Exercicio_fixacao.applications;

import Secao_16.Aula_177.Exercicio_fixacao.entities.Contract;
import Secao_16.Aula_177.Exercicio_fixacao.entities.Installment;
import Secao_16.Aula_177.Exercicio_fixacao.service.ContractService;
import Secao_16.Aula_177.Exercicio_fixacao.service.PaypalService;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        DateTimeFormatter dtm = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        System.out.println("Entre os dados do contrato: ");

        System.out.print("Numero: ");
        int number = sc.nextInt();

        System.out.print("Data (dd/MM/yyyy): ");
        LocalDate date = LocalDate.parse(sc.next(), dtm);

        System.out.print("Valor do contrato: ");
        double totalValue = sc.nextDouble();

        System.out.print("Entre com o numero de parcelas: ");
        int valueContract = sc.nextInt();

        Contract contract = new Contract(number, date, totalValue);

        ContractService service = new ContractService(new PaypalService());

        service.processContract(contract, valueContract);

        System.out.println("Parcelas:");

        for (Installment inst : contract.getInstallmentList()) {
            System.out.println(dtm.format(inst.getDate()) + " - " + String.format("%.2f", inst.getAmount()));
        }
    }
}
