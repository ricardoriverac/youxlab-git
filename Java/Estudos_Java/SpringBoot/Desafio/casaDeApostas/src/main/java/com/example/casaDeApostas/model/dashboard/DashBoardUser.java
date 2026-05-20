package com.example.casaDeApostas.model.dashboard;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class DashBoardUser {

    private Long totalJogos;

    private Integer ganhos;

    private Integer perdas;

    public DashBoardUser(Long totalJogos, Integer ganhos, Integer perdas) {
        this.totalJogos = totalJogos;
        this.ganhos = ganhos;
        this.perdas = perdas;
    }
}
