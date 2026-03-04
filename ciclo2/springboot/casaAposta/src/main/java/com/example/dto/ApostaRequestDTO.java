package com.example.dto;

public class ApostaRequestDTO {

    @NotNull(message = "Valor da aposta é obrigatório")
    @Positive(message = "Valor deve ser positivo")
    private Double valorApostado;

    public Double getValorApostado() { return valorApostado; }
    public void setValorApostado(Double valorApostado) { this.valorApostado = valorApostado; }
}
