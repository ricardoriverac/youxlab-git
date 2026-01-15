package application.entities;

public interface ServicoPagamentoOnline {
    Double taxaPagamento(double valor);
    Double parcela(double valor, Integer mes);

}
