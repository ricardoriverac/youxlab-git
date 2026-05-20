package com.example.casaDeApostas.dto;

import com.example.casaDeApostas.model.users.User;

import java.math.BigDecimal;
import java.util.UUID;

public record CriarJogoDTO(UUID userId, Double valorAposta){
}
