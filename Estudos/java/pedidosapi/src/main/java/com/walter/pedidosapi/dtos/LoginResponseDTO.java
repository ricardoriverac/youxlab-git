package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;

@Schema(name = "LoginResponse")
public record LoginResponseDTO(
        @Schema(name = "token")
        @JsonProperty("token")
        String token
) {
}