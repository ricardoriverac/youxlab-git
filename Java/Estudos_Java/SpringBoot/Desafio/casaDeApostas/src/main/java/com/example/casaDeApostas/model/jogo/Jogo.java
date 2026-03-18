package com.example.casaDeApostas.model.jogo;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;
import lombok.Data;

import java.util.*;

@Entity
@Table(name = "Jogos")
@Data
public class Jogo {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID idJogo;

    @NotNull
    private UUID idUsuario;

}
