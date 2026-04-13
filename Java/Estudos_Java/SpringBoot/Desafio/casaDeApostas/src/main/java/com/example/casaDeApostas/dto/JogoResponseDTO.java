package com.example.casaDeApostas.dto;

import com.example.casaDeApostas.model.enums.TipoCampo;

public record JogoResponseDTO(

        Double valorApostado,
        TipoCampo tipo
) {}
