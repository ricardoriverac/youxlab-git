package Secao16.aula183;

public class Program {

    public static void main(String[] args) {
        BraziInterestService service = new BraziInterestService(2.0); // Taxa de 2%
        double amount = 200.00;
        int months = 3;
        double paymentValue = service.payment(amount, months);
        System.out.printf("Payment after %d months: %.2f%n", months, paymentValue);
    }
}
