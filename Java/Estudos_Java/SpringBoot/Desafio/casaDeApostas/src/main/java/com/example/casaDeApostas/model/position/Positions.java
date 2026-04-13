package com.example.casaDeApostas.model.position;

import com.example.casaDeApostas.model.enums.TipoCampo;
import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.UUID;

@Entity
@Table(name = "positions")
@Data
@NoArgsConstructor
public class Positions {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @NotNull
    private int linha;

    @NotNull
    private int coluna;

    @NotNull
    @Enumerated(EnumType.STRING)
    private TipoCampo tipo;

    public Positions(int linha, TipoCampo tipo) {
        this.linha = linha;
        this.tipo = tipo;
    }
}
