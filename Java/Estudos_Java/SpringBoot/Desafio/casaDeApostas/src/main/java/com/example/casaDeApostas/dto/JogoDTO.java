package com.example.casaDeApostas.dto;

import com.example.casaDeApostas.model.enums.TipoJogo;

import java.util.UUID;

public record JogoDTO(
        UUID idJogo,
        Double valorDoJogo,
        TipoJogo tipoJogo
) {
}
