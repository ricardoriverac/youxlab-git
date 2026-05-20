package com.example.casaDeApostas.dto;

import com.example.casaDeApostas.model.enums.Roles;
import com.fasterxml.jackson.annotation.JsonIgnore;

public record LoginDTO(String email, String senha, Roles role) {
}
