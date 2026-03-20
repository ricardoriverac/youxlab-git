package com.walter.pedidosapi.dtos;


import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.NotNull;

import java.util.List;
import java.util.UUID;

@Schema(name = "OrderRegister")
public record OrderRegisterDTO(

        @NotNull(message = "é obrigatório um pedido ter o id de seu usuário")
        @Schema(name = "idUsuario")
        @JsonProperty("idUsuario")
        UUID userId,
        @NotEmpty(message = "o pedido não pode ser vazio")
        @Schema(name = "itens")
        @JsonProperty("itens")
        List<OrderItemRegisterDTO> items
) {
}