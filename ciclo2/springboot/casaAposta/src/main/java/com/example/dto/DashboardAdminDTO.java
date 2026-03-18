package com.example.dto;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

public class DashboardAdminDTO{

    @JsonProperty("valorTotalGanho")
    private BigDecimal valorTotalGanho;


    @JsonProperty("maiorGanho")
    private BigDecimal maiorGanho;


    @JsonProperty("totalUser")
    private Long totalUser;


    @JsonFormat(pattern = "dd/MM/yyyy HH:mm")
    @JsonProperty("dataAtualizacao")
    private String dataAtualizacao;


    public DashboardAdminDTO() {
        this.dataAtualizacao = java.time.LocalDateTime.now()
                .format(java.time.format.DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
    }


    public BigDecimal getValorTotalGanho() {
        return valorTotalGanho;
    }

    public void setValorTotalGanho(BigDecimal valorTotalGanho) {
        this.valorTotalGanho = valorTotalGanho;
    }

    public void setMaiorGanho(BigDecimal maiorGanho) {
        this.maiorGanho = maiorGanho;
    }

    public void setTotalUser(Long totalUser) {
        this.totalUser = totalUser;
    }
}


