package application.entities;

public class PayPal implements ServicoPagamentoOnline{
    @Override
    public Double taxaPagamento(double valor){
        return valor * 0.02;
    }
    @Override
    public Double parcela(double valor, Integer mes){
        return valor = valor * 0.01 * mes;
    }
}
