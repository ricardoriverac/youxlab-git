package Secao_16.Aula_174.Solucao_do_problema_PARTE_2.application;

import Secao_16.Aula_174.Solucao_do_problema_PARTE_2.entities.CarRental;
import Secao_16.Aula_174.Solucao_do_problema_PARTE_2.entities.Vehicle;
import Secao_16.Aula_174.Solucao_do_problema_PARTE_2.model.services.BrazilTaxService;
import Secao_16.Aula_174.Solucao_do_problema_PARTE_2.model.services.RentalService;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Entre com os dados do aluguel");

        System.out.print("Modelo do carro: ");
        String carModel = sc.nextLine();

        System.out.print("Retirada (dd/MM/yyyy hh:mm): ");
        LocalDateTime start = LocalDateTime.parse(sc.nextLine(), fmt);

        System.out.print("Retorno (dd/MM/yyyy hh:mm): ");
        LocalDateTime finish = LocalDateTime.parse(sc.nextLine(), fmt);

        CarRental cr = new CarRental(start, finish, new Vehicle(carModel));

        System.out.print("Entre com o preço por hora: ");
        double pricePerHour = sc.nextDouble();

        System.out.print("Entre com o preço por dia: ");
        Double priceperDay = sc.nextDouble();

        RentalService rentalService = new RentalService(pricePerHour, priceperDay, new BrazilTaxService());

        rentalService.processInvoice(cr);

        System.out.println("FATURA:");

        System.out.println("Pagamento basico: " + String.format("%.2f", cr.getInvoice().getBasicPayment()));
        System.out.println("Imposto: " + String.format("%.2f", cr.getInvoice().getTax()));
        System.out.println("Pagamento total: " + String.format("%.2f", cr.getInvoice().getTotalPayment()));

        sc.close();
    }
}