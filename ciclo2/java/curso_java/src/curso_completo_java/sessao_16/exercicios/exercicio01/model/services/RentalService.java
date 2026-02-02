package curso_completo_java.sessao_16.exercicios.exercicio01.model.services;

import curso_completo_java.sessao_16.exercicios.exercicio01.model.entities.CarRental;
import curso_completo_java.sessao_16.exercicios.exercicio01.model.entities.Invoice;

import java.time.Duration;

public class RentalService {

        private Double pricePerDay;
        private Double pricePerHour;

        private TaxService taxService;

        public RentalService(Double pricePerDay, Double pricePerHour, TaxService taxService) {
            this.pricePerDay = pricePerDay;
            this.pricePerHour = pricePerHour;
            this.taxService = taxService;
        }

        public void processInvoice(CarRental carRental) {

            double minutes = Duration.between(carRental.getStart(), carRental.getFinish()).toMinutes();
            double hours = minutes / 60.0;

            double basicPayment;
            if (hours <= 12.0) {
                basicPayment = pricePerHour * Math.ceil(hours);
            }
            else {
                basicPayment = pricePerDay * Math.ceil(hours / 24);
            }

            double tax = taxService.tax(basicPayment);

            carRental.setInvoice(new Invoice(basicPayment, tax));
        }
    }

