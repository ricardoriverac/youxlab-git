package com.example.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.Valid;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;

@Valid
public record LoginRequestDTO(

        @NotBlank(message = "Email é obrigatório")
        @Email(message = "Email inválido")
        @JsonProperty("email")
                String email,

        @NotBlank(message = "Senha é obrigatória")
        @Pattern(
                regexp = "^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>\\/?]).{8,}$",
                message = "Senha deve conter pelo menos uma letra maiúscula, um número e um caractere especial"
        )        @JsonProperty("senha")
        String senha

) {
}
