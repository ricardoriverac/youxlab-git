package com.example.dto;

import com.example.enuns.StatusJogo;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.math.BigDecimal;
import java.time.LocalDateTime;

public record JogoResponseDTO(

        @JsonProperty("jogoId")
                Long jogoId,

        @JsonProperty("valorAposta")
        BigDecimal valorAposta,

        @JsonProperty("valorAcumulado")
        BigDecimal valorAcumulado,

        @JsonProperty("status")
        StatusJogo status,

        @JsonProperty("diamantesEncontrados")
        Integer diamantesEncontrados,

        @JsonProperty("tabuleiro")
        String[][] tabuleiro,

        @JsonProperty("jogadasRestantes")
        Integer jogadasRestantes,

        @JsonProperty("totalDiamantes")
        Integer totalDiamantes,

        @JsonProperty("totalBombas")
        Integer totalBombas,

        @JsonProperty("mensagem")
        String mensagem,

        @JsonFormat(pattern = "dd/MM/yyyy HH:mm")
        @JsonProperty("dataInicio")
        LocalDateTime dataInicio

) {
    public JogoResponseDTO(Long jogoId, BigDecimal valorAposta, BigDecimal valorAcumulado,
                           StatusJogo status, Integer diamantesEncontrados, String[][] tabuleiro) {
        this(
                jogoId,
                valorAposta,
                valorAcumulado,
                status,
                diamantesEncontrados,
                tabuleiro,
                10 - diamantesEncontrados,
                10,
                15,
                gerarMensagemStatus(status, diamantesEncontrados, valorAcumulado),
                LocalDateTime.now()
        );
    }


    private static String gerarMensagemStatus(StatusJogo status, Integer diamantes, BigDecimal valor) {
        switch (status) {
            case EM_ANDAMENTO:
                return " Jogo em andamento \n" + "Encontrou: " + diamantes + " diamantes\n" + "Prêmio atual: R$ " + valor;
            case GANHOU:
                return " Parabéns! Você encontrou todos os 10 diamantes! Ganhou R$ " + valor;
            case PERDEU:
                return " boom! Você encontrou uma bomba e perdeu tudo";
            case ENCERRADO:
                return " Jogo encerrado\n" + "Você ganhou R$" + valor;
            default:
                return "";
        }
    }

}

