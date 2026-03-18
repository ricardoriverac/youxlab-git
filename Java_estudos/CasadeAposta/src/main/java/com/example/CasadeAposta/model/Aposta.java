package com.example.CasadeAposta.model;

import com.example.CasadeAposta.model.enums.ApostaStatus;
import jakarta.persistence.*;
import lombok.*;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Aposta {

        @Id
        @GeneratedValue
        private UUID id;

        private BigDecimal valorApostado;

        @Column(name = "valor_ganhos")
        private BigDecimal valorGanhos;

        @Enumerated(EnumType.STRING)
        private ApostaStatus status;

        private LocalDateTime dataCriacao = LocalDateTime.now();


        private LocalDateTime dataEncerramento;

        @ManyToOne
        @JoinColumn(name = "usuario_id")
        private User usuario;

        private int diamantesEncontrados;


        private BigDecimal valorAtual;

    }