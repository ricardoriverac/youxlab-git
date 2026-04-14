package Secao_16.Aula_177.Exercicio_fixacao.service;

import Secao_16.Aula_177.Exercicio_fixacao.interfece.OnlinePaymentService;

public class PaypalService implements OnlinePaymentService {

    @Override
    public Double paymentFee(Double amount) {
        return amount * 0.02;
    }

    @Override
    public Double interest(Double amount, Integer months) {
        return  amount * (0.01 * months);
    }
}