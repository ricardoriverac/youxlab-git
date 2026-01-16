package secao_16.aula_173.application;

import secao_16.aula_173.model.entities.CarRental;
import secao_16.aula_173.model.entities.Vehicle;
import secao_16.aula_173.model.services.BrazilTaxService;
import secao_16.aula_173.model.services.RetalService;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class Program {
    static void main() {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");


        System.out.println("Entre com os dados do aluguel: ");
        System.out.print("Modelo do carro: ");
        String carMOdel = sc.nextLine();
        System.out.println("Retirada (dd/MM/yyyy hh:mm ): ");
        LocalDateTime start = LocalDateTime.parse(sc.nextLine(),fmt);
        System.out.println("Retirada (dd/MM/yyyy hh:mm ): ");
        LocalDateTime finish = LocalDateTime.parse(sc.nextLine(),fmt);


        CarRental cr = new CarRental(start, finish, new Vehicle(carMOdel));
        System.out.print("Entre com o preço por hora: ");
        double pricePerHour = sc.nextDouble();
        System.out.print("Entre com o preço por dia: ");
        double pricePerDay = sc.nextDouble();

        RetalService retalService = new RetalService(pricePerHour,pricePerDay, new BrazilTaxService());
        retalService.processesInvoice(cr);

        System.out.println("FATURA: ");
        System.out.println("Pagamento basico: " + cr.getInvoice().getBasicPayment());
        System.out.println("Inposto: ");
        System.out.println("Pagamento total: " + cr.getInvoice().getTotalPayment());



    }
}
