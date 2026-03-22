package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;

@Schema(name = "RegisterResponse")
public record RegisterResponseDTO(
        @Schema(name = "nome")
        @JsonProperty("nome")String name,
        @Schema(name = "email")
        @JsonProperty("email")String email
) {
}