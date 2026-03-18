package com.example.CasadeAposta.dtos;

import com.example.CasadeAposta.model.enums.Papel;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;

import java.time.LocalDate;

public record AuthDTO(

        @NotBlank
        String nome,

        @Email
        String email,

        @NotBlank
        LocalDate dataNascimento,

        @Pattern(
                regexp = "^(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&]).{8,}$",
                message = "Senha deve ter 8 caracteres, uma maiúscula, número e símbolo"
        )
        String senha,

        @NotBlank
        String confirmarSenha,

        @NotBlank
        Papel role


) {}
