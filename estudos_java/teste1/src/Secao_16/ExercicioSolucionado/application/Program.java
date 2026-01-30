package Secao_16.ExercicioSolucionado.application;

import Secao_16.ExercicioSolucionado.model.entities.CarRental;
import Secao_16.ExercicioSolucionado.model.entities.Vehicle;
import Secao_16.ExercicioSolucionado.model.services.BrazilTaxService;
import Secao_16.ExercicioSolucionado.model.services.RentalService;

import java.text.ParseException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class Program {

    public static void main(String[] args) throws ParseException {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
        System.out.println("Entre com os dados do aluguel");
        System.out.print("Modelo do carro: ");
        String carModel = sc.nextLine();
        System.out.print("Retirada (dd/Mm/yy hh:mm):");
        LocalDateTime start = LocalDateTime.parse(sc.nextLine(), fmt);
        System.out.print("Retorno (dd/Mm/yy hh:mm):");
        LocalDateTime finish = LocalDateTime.parse(sc.nextLine(), fmt);

        CarRental cr = new CarRental(start, finish, new Vehicle(carModel));

        System.out.println("Entre com o preço por hora: ");
        double pricePerHour = sc.nextDouble();
        System.out.println("Entre com o preço por dia: ");
        double pricePerDay = sc.nextDouble();

        RentalService rentalService = new RentalService(pricePerHour, pricePerDay, new BrazilTaxService());

        rentalService.processInvoice(cr);

        System.out.println("--- RECEIPT ---");
        System.out.println("Basic payment: " + String.format("%.2f",cr.getInvoice().getBasicPayment()));
        System.out.println("Tax: " + String.format("%.2f",cr.getInvoice().getTax()));
        System.out.println("Total payment: " + String.format("%.2f",cr.getInvoice().getTotalPayment()));

        sc.close();
    }

}
