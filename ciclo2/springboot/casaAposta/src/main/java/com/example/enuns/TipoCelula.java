package com.example.enuns;

public enum TipoCelula {


    DIAMANTE("diamante"),
    DIAMANTE_VITORIA("diamante_vitoria"),
    BOMBA("bomba"),
    JA_REVELADO("ja_revelado"),
    NAO_REVELADO("nao_revelado");

    private final String tipo;
    TipoCelula(String tipo) {
        this.tipo = tipo;
    }
}

