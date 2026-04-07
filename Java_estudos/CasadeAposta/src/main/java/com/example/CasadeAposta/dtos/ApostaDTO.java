package com.example.CasadeAposta.dtos;

import com.example.CasadeAposta.model.enums.ApostaStatus;
import java.math.BigDecimal;

public record ApostaDTO(
        BigDecimal valorApostado,
        BigDecimal valorAtual,
        int diamantesEncontrados,
        ApostaStatus status,
        BigDecimal valorGanhos
) {}
