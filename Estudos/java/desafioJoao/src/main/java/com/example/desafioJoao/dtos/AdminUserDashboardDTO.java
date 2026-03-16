package com.example.desafioJoao.dtos;

import java.math.BigDecimal;

public record AdminUserDashboardDTO(
        String name,
        int totalGames,
        BigDecimal totalGain
) {
}
