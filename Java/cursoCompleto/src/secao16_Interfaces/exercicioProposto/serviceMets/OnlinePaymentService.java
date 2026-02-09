package secao16_Interfaces.exercicioProposto.serviceMets;

public interface OnlinePaymentService {

    Double paymentFee(Double amount);
    Double interest(Double amount, Integer months);
}
