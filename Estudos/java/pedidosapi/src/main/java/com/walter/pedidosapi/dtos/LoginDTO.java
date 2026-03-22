package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;

@Schema(name = "Login")
public record LoginDTO(
        @Schema(name = "email")
        @JsonProperty("email")
        String email,
        @Schema(name = "senha")
        @JsonProperty("senha")
        String password
) {
}