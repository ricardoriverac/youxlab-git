package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;

import java.math.BigDecimal;
import java.util.UUID;

@Schema(name = "ProductResponse")
public record ProductResponseDTO(
        @Schema(name = "id")
        @JsonProperty("id")
        UUID id,
        @Schema(name = "nome")
        @JsonProperty("nome")
        String name,
        @Schema(name = "descricao")
        @JsonProperty("descricao")
        String description,
        @Schema(name = "preco")
        @JsonProperty("preco")
        BigDecimal price,
        @Schema(name = "quantidadeEstoque")
        @JsonProperty("quantidadeEstoque")
        int stockQuantity
) {
}