package Secao16.aula172;

import java.time.Duration;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

        System.out.println("Entre com os dados do aluguel: ");
        System.out.print("Modelo do carro: ");
        String carModel = sc.nextLine();

        System.out.print("Retirada (dd/MM/yyyy HH:mm): ");
        LocalDateTime start = LocalDateTime.parse(sc.nextLine(), fmt);

        System.out.print("Retorno (dd/MM/yyyy HH:mm): ");
        LocalDateTime finish = LocalDateTime.parse(sc.nextLine(), fmt);

        System.out.print("Digite o preço por hora: ");
        double pricePerHour = sc.nextDouble();

        System.out.print("Digite o preço por dia: ");
        double pricePerDay = sc.nextDouble();

        Veiculo veiculo = new Veiculo(carModel);
        carRental carRental = new carRental(start, finish, veiculo);

        Duration duration = Duration.between(start, finish);
        long totalMinutes = duration.toMinutes();
        long hours = totalMinutes / 60;
        long minutes = totalMinutes % 60;
        int roundedHours;

        if (minutes > 0) {
            roundedHours = (int) hours + 1;
        } else {
            roundedHours = (int) hours;
        }
        double basicPay;
        if (roundedHours <= 12) {
            basicPay = roundedHours * pricePerHour;
        } else {
            int roundedDays = (roundedHours % 24 == 0) ? roundedHours / 24 : (roundedHours / 24) + 1;
            basicPay = roundedDays * pricePerDay;
        }
        double tax = basicPay * 0.20;
        if (basicPay > 100) {
            tax = basicPay * 0.15;
        }

        carRental.setInvoice(new Invoice(basicPay, tax));

        System.out.println("\nINVOICE:");
        System.out.printf("Basic payment: %.2f%n", carRental.getInvoice().getBasicpay());
        System.out.printf("Tax: %.2f%n", carRental.getInvoice().getTax());
        System.out.printf("Total payment: %.2f%n", carRental.getInvoice().getTotalPayment());



        sc.close();
    }
}
