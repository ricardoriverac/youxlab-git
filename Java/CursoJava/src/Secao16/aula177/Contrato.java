package Secao16.aula177;

import java.time.LocalDate;

public class Contrato {
    private Integer numero;
    private LocalDate data;
    private Double valorTotal;

    public Contrato(Integer numero, LocalDate data, Double valorTotal) {
        this.numero = numero;
        this.data = data;
        this.valorTotal = valorTotal;
    }

    public Integer getNumero() {
        return numero;
    }

    public LocalDate getData() {
        return data;
    }

    public Double getValorTotal() {
        return valorTotal;
    }
}
