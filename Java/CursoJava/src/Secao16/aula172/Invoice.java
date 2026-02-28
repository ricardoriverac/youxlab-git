package Secao16.aula172;

public class Invoice {
    private double basicpay;
    private double tax;

    public Invoice(double basicpay, double tax){
        this.basicpay = basicpay;
        this.tax = tax;
    }
    public double getBasicpay() {
        return basicpay;
    }
    public double getTax() {
        return tax;
    }
    public double getTotalPayment() {
        return basicpay + tax;
    }
}
