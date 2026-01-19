package curso_completo_java.sessao_16.exercicios.exercicio02.services;

public interface OnlinePaymentService {

    double paymentFee (double amount);
    double interest (double amount, int months);
}

