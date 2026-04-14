package Secao_16.Aula_177.Exercicio_fixacao.service;

public interface OnlinePaymentService {

    public Double paymentFee(Double amount);

    public Double interest(Double amount, Integer months);
}
