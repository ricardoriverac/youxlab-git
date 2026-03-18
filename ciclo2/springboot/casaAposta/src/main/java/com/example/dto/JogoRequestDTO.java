package com.example.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.NotNull;

import java.math.BigDecimal;

public record JogoRequestDTO(

        @NotNull(message = "ID do usuário é obrigatório")
        @JsonProperty("userId")
                Long userId,

        @NotNull(message = "Valor da aposta é obrigatório")
        @DecimalMin(value = "1.0", message = "Valor da aposta deve ser no mínimo R$ 1,00")
        @JsonProperty("valorAposta")
        BigDecimal valorAposta

) {
}
