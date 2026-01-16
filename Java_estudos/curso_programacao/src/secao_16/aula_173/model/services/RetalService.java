package secao_16.aula_173.model.services;

import secao_16.aula_173.model.entities.CarRental;
import secao_16.aula_173.model.entities.Invoice;

import java.time.Duration;

public class RetalService {

    private Double pricePerHour;
    private Double pricePerDay;

    private BrazilTaxService taxService;

    public RetalService(Double pricePerHour, Double pricePerDay, BrazilTaxService taxService) {
        this.pricePerHour = pricePerHour;
        this.pricePerDay = pricePerDay;
        this.taxService = taxService;
    }

    public void processesInvoice(CarRental carRental){
        long minutes = Duration.between(carRental.getStart(), carRental.getFinish()).toMinutes();
        double hours = minutes / 60.0;

        double basicPayment;
        if (hours <= 12.0){
            basicPayment = pricePerHour * Math.ceil(hours);
        }else {
            basicPayment = pricePerDay * Math.ceil(hours / 24.0);
        }
        carRental.setInvoice(new Invoice(50.0, 10.0));
    }
}
