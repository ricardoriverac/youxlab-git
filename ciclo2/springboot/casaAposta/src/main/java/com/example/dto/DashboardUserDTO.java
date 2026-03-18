package com.example.dto;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;

public class DashboardUserDTO{

    @JsonProperty("totalGanho")
    private BigDecimal totalGanho;



    @JsonProperty("mediaAposta")
    private BigDecimal mediaAposta;

    @JsonProperty("saldo")
    private BigDecimal saldo;


    @JsonProperty("totalDiamantesEncontrados")
    private Long totalDiamantesEncontrados;

    @JsonProperty("totalBombasEncontradas")
    private Long totalBombasEncontradas;


    @JsonFormat(pattern = "dd/MM/yyyy HH:mm")
    @JsonProperty("dataAtualizacao")
    private String dataAtualizacao;

    @JsonProperty("nivelJogador")
    private String nivelJogador;


    public DashboardUserDTO() {
        this.dataAtualizacao = java.time.LocalDateTime.now()
                .format(java.time.format.DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
    }


    public void setTotalGanho(BigDecimal totalGanho) {
        this.totalGanho = totalGanho;
    }

    public void setMediaAposta(BigDecimal mediaAposta) {
        this.mediaAposta = mediaAposta;
    }



    public void setTotalDiamantesEncontrados(Long totalDiamantesEncontrados) {
        this.totalDiamantesEncontrados = totalDiamantesEncontrados;
    }

    public void setTotalBombasEncontradas(Long totalBombasEncontradas) {
        this.totalBombasEncontradas = totalBombasEncontradas;
    }

}

