package com.example.desafioJoao.dtos;

import jakarta.validation.constraints.Digits;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;

import java.math.BigDecimal;

public record BetDTO(
        @NotNull
        @Positive
        @Digits(integer = 8, fraction = 2)
        BigDecimal betValue) {
}
