package Secao16.aula177;

import java.time.LocalDate;

public class Parcela {
    private LocalDate dataVencimento;
    private Double valor;

    public Parcela(LocalDate dataVencimento, Double valor) {
        this.dataVencimento = dataVencimento;
        this.valor = valor;
    }

    public LocalDate getDataVencimento() {
        return dataVencimento;
    }

    public Double getValor() {
        return valor;
    }
}
