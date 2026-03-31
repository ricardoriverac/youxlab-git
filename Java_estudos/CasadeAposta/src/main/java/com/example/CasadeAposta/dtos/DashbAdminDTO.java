package com.example.CasadeAposta.dtos;

import java.math.BigDecimal;

public record DashbAdminDTO(
        long totalJogos,
        BigDecimal totalGanhos
)  {
}
