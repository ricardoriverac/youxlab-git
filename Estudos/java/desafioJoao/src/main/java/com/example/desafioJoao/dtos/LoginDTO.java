package com.example.desafioJoao.dtos;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;


public record LoginDTO(
        @Email
        @NotBlank
        String email,
        @Pattern(regexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&]).{8,}$", message = "A senha deve ter no mínimo 8 caracteres, uma letra maíuscula, uma letra minúscula, um número e um caractere especial")
        @Size(min = 8)
        @NotBlank
        String password
) {
}
