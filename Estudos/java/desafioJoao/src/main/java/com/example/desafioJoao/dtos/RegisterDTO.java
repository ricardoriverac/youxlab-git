package com.example.desafioJoao.dtos;


import jakarta.validation.constraints.*;

import java.time.LocalDate;

public record RegisterDTO(
        @NotBlank
        String name,
        @Email
        @NotBlank
        String email,
        @NotNull
        LocalDate birthDate,
        @NotBlank
        @Pattern(regexp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&]).{8,}$", message = "A senha deve ter no mínimo 8 caracteres, uma letra maíuscula, uma letra minúscula e um número e um caractere especial")
        @Size(min = 8)
        String password,
        @NotBlank
        String confirmPassword
){}
