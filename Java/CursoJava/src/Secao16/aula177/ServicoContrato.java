package Secao16.aula177;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class ServicoContrato {
    private static final double TAXA_JUROS = 0.01;

    public List<Parcela> gerarParcelas(Contrato contrato, int numeroParcelas) {
        List<Parcela> parcelas = new ArrayList<>();
        Double valorParcelaBase = contrato.getValorTotal() / numeroParcelas;

        for (int i = 1; i <= numeroParcelas; i++) {
            LocalDate dataVencimento = contrato.getData().plusMonths(i);
            Double valorParcela = valorParcelaBase * Math.pow(1 + TAXA_JUROS, i);
            valorParcela = Math.round(valorParcela * 100.0) / 100.0;
            parcelas.add(new Parcela(dataVencimento, valorParcela));
        }

        return parcelas;
    }
}
