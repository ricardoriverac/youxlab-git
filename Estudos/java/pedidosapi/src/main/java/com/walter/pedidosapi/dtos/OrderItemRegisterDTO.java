package com.walter.pedidosapi.dtos;


import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;

import java.util.UUID;

@Schema(name = "OrderItemRegister")
public record OrderItemRegisterDTO(
        @NotNull(message = "é obrigatório o item ter o id de seu pedido")
        @Schema(name = "idProduto")
        @JsonProperty("idProduto")
        UUID productId,
        @Positive(message = "a quantidade tem que ser maior que zero")
        @NotNull(message = "a quantidade não pode ser nula")
        @Schema(name = "quantidade")
        @JsonProperty("quantidade")
        int quantity
) {
}