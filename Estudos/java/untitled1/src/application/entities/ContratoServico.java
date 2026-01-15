package application.entities;


import java.time.LocalDate;
import java.time.LocalDateTime;


public class ContratoServico {
    private  ServicoPagamentoOnline servicoPagamentoOnline;
    public ContratoServico() {
    }

    public ContratoServico(ServicoPagamentoOnline servicoPagamentoOnline) {
        this.servicoPagamentoOnline = servicoPagamentoOnline;
    }

    public void processContrato(Contrato contrato, int mes) {
        Double valorMedia = contrato.getValorTotal() / mes;
        for (int i = 0; i < mes; i++) {
            LocalDate dataParcela = contrato.getDataContrato().plusMonths(i);
            Double taxaPagamento = servicoPagamentoOnline.taxaPagamento(valorMedia);
            Double parcela = servicoPagamentoOnline.parcela(valorMedia, i + 1);
            Double valorParcela = valorMedia + taxaPagamento + parcela;
            contrato.getParcelas().add(new Parcelas(dataParcela, valorParcela));
        }
    }
}