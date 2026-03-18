package com.example.CasadeAposta.dtos;

import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;

import java.math.BigDecimal;

public record CriarApostaDTO(

        @NotNull
        @Positive
        BigDecimal valor_apostado
) {

}
