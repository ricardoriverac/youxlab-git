package com.example.casaDeApostas.dto;

import com.example.casaDeApostas.model.enums.TipoJogo;

import java.util.UUID;

public record EncerrarDTO(UUID id, TipoJogo tipo) {
}
