package com.example.desafioJoao.dtos;


import com.example.desafioJoao.enums.BetStatus;

import java.math.BigDecimal;
import java.util.UUID;

public record BetResponseDTO(
        UUID id,
        BetStatus status,
        BigDecimal betValue,
        BigDecimal gainValue,
        int quantityDiamonds
) {
}
