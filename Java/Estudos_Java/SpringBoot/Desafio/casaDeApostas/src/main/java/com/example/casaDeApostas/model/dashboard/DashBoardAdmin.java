package com.example.casaDeApostas.model.dashboard;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class DashBoardAdmin {

    private Long totalJogos;

    private Double valorDosJogos;

    public DashBoardAdmin(Long totalJogos, Double valorDosJogos) {
        this.totalJogos = totalJogos;
        this.valorDosJogos = valorDosJogos;
    }
}
