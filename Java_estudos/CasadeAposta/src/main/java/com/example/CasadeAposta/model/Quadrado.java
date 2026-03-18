package com.example.CasadeAposta.model;

import com.example.CasadeAposta.model.enums.TipoQuadrado;
import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.Id;
import lombok.*;

import java.math.BigDecimal;
import java.util.UUID;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Quadrado {

    @Id
    @JsonIgnore
    private UUID id;
    private int linha;

    private int coluna;

    private boolean revelado;

    private TipoQuadrado tipo;

    private BigDecimal valorAtual;




}