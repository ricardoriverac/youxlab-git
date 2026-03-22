package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;

import java.time.LocalDateTime;
import java.util.UUID;

@Schema(name = "UserResponse")
public record UserResponseDTO(
        @Schema(name = "id")
        @JsonProperty("id")
        UUID id,
        @Schema(name = "nome")
        @JsonProperty("nome")String name,
        @Schema(name = "email")
        @JsonProperty("email")String email,
        @Schema(name = "cargo")
        @JsonProperty("role") String role,
        @Schema(name = "criadoEm")
        @JsonProperty("criadoEm") LocalDateTime createdAt
) {

}