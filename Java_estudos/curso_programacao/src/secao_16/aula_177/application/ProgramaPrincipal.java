package secao_16.aula_177.application;

import secao_16.aula_177.model.entities.Contract;
import secao_16.aula_177.model.entities.Installment;
import secao_16.aula_177.model.services.ContractService;
import secao_16.aula_177.model.services.PaypalService;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class ProgramaPrincipal {
    public static void main(String[] args) throws ParseException {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        System.out.println("Entre os dados do comtrato: ");
        System.out.println("Numero: ");
        int numero = sc.nextInt();
        System.out.println("Data (dd/MM/yyyy): ");
        LocalDate dateD = LocalDate.parse(sc.next(),fmt);
        System.out.println("Valor do contrato: ");
        double valor = sc.nextDouble();


        Contract obj = new Contract(numero, dateD, valor);

        System.out.print("Entre com o numero de parcelas: ");
        int n = sc.nextInt();

        ContractService contractService = new ContractService(new PaypalService());

        contractService.processContract(obj, n);

        System.out.println("Parcelas:");
        for (Installment installment : obj.getInstallments()) {
            System.out.println(installment);
        }

        sc.close();
    }
}
