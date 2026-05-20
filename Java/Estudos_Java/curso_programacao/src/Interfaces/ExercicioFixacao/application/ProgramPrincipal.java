package Interfaces.ExercicioFixacao.application;

import Interfaces.ExercicioFixacao.model.entities.Contract;
import Interfaces.ExercicioFixacao.model.entities.Installment;
import Interfaces.ExercicioFixacao.model.services.ContractService;
import Interfaces.ExercicioFixacao.model.services.PaypalService;

import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class ProgramPrincipal {
    static void main() {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        DateTimeFormatter dmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        System.out.println("Entre os dados do contrato:");
        System.out.print("Numero: ");
        int numero = sc.nextInt();
        System.out.print("Data (DD/MM/YYYY): ");
        sc.nextLine();
        LocalDate date = LocalDate.parse(sc.nextLine(), dmt);
        System.out.print("Valor do contrato: ");
        double valorContrato = sc.nextDouble();
        System.out.print("Entre com o numero de parcelas: ");
        int numeroParcelas = sc.nextInt();

        Contract contract = new Contract(numero, date, valorContrato);

        ContractService contractService = new ContractService(new PaypalService());
        contractService.processContract(contract, numeroParcelas);

        System.out.println("FATURA:");

        for (Installment installment : contract.getInstallments()){
            System.out.print(installment);
        }
        sc.close();
    }
}
