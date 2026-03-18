package com.example.dto;

import com.example.enuns.StatusJogo;
import com.example.enuns.TipoCelula;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.math.BigDecimal;

public record JogadaResponseDTO(

        @JsonProperty("tipoCelula")
                String tipoCelula,

        @JsonProperty("valorAcumulado")
        BigDecimal valorAcumulado,

        @JsonProperty("status")
        String status,

        @JsonProperty("jogoFinalizado")
        Boolean jogoFinalizado,

        @JsonProperty("diamantesEncontrados")
        Integer diamantesEncontrados,

        @JsonProperty("mensagem")
        String mensagem,

        @JsonProperty("podeEncerrar")
        Boolean podeEncerrar,

        @JsonProperty("proximoPremio")
        BigDecimal proximoPremio

) {
    public JogadaResponseDTO(TipoCelula tipoCelula, BigDecimal valorAcumulado,
                             StatusJogo status, Boolean jogoFinalizado, String mensagem) {
        this(
                tipoCelula != null ? tipoCelula.name() : null,
                valorAcumulado,
                status != null ? status.name() : null,
                jogoFinalizado,
                null,
                mensagem,
                status == StatusJogo.EM_ANDAMENTO,
                null
        );
    }


}

