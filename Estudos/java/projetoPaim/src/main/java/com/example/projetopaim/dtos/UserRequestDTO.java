package com.example.projetopaim.dtos;

import jakarta.persistence.UniqueConstraint;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public record UserRequestDTO(
        @NotBlank(message = "Email obrigatório!")
        @Email
        String email,
        @NotBlank(message = "senha obrigatória!")
        String password
){}

