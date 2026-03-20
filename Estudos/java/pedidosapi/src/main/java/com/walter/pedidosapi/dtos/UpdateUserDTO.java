package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

@Schema(name = "UpdateUser")
public record UpdateUserDTO(
        @NotBlank
        @Schema(name = "nome")
        @JsonProperty("nome")
        String name,
        @Email
        @NotBlank
        @Schema(name = "email")
        @JsonProperty("email")
        String email
) {
}