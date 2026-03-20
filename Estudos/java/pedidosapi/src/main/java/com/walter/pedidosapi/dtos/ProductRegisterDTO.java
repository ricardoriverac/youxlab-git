package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.*;

import java.math.BigDecimal;

@Schema(name = "ProductRegister")
public record ProductRegisterDTO(
        @NotBlank(message = "é obrigatório o produto ter um nome")
        @Schema(name = "nome")
        @JsonProperty("nome")
        String name,
        @Schema(name = "descricao")
        @JsonProperty("descricao")
        String description,
        @NotNull(message = "é obrigatório o produto ter um preço")
        @Positive(message = "é obrigatório o valor do produto ser positivo")
        @Digits(integer = 8, fraction = 2, message = "o preço do produto deve ter 8 digitos e duas casas decimais")
        @Schema(name = "preco")
        @JsonProperty("preco")
        BigDecimal price,
        @NotNull(message = "a quantidade em estoque não pode ser nula")
        @PositiveOrZero(message = "a quantidade em estoque não pode ser negativa")
        @Schema(name = "quantidadeEstoque")
        @JsonProperty("quantidadeEstoque")
        Integer stockQuantity

) {
}