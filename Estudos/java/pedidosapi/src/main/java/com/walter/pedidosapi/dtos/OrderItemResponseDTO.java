package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;

import java.math.BigDecimal;
import java.util.UUID;

@Schema(name = "OrderItemResponse")
public record OrderItemResponseDTO(
        @Schema(name = "id")
        @JsonProperty("id")
        UUID id,
        @Schema(name = "quantidade")
        @JsonProperty("quantidade")
        int quantity,
        @Schema(name = "precoUnitario")
        @JsonProperty("precoUnitario")
        BigDecimal unitPrice,
        @Schema(name = "idProduto")
        @JsonProperty("idProduto")
        UUID productId
) {
}