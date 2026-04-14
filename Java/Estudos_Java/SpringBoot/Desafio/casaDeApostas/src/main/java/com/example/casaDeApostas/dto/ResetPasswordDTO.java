package com.example.casaDeApostas.dto;

import com.example.casaDeApostas.model.enums.Roles;

import java.time.LocalDate;

public record AdminDTO(String name, String email, LocalDate dataNascimento, String senha, String confirmacaoSenha, Roles role, Long cpf) {
}
