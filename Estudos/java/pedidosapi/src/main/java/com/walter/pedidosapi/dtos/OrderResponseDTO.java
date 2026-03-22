package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.walter.pedidosapi.models.OrderItem;

import io.swagger.v3.oas.annotations.media.Schema;
import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

@Schema(name = "OrderResponse")
public record OrderResponseDTO(
        @Schema(name = "id")
        @JsonProperty("id")
        UUID id,
        @Schema(name = "dataPedido")
        @JsonProperty("dataPedido")
        LocalDateTime orderDate,
        @Schema(name = "valorTotal")
        @JsonProperty("valorTotal")
        BigDecimal totalValue,
        @Schema(name = "itens")
        @JsonProperty("itens")
        List<OrderItemResponseDTO> items,
        @Schema(name = "idUsuario")
        @JsonProperty("idUsuario")
        UUID userId
) {
}