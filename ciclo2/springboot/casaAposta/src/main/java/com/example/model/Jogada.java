package com.example.model;

import com.example.enuns.TipoCelula;
import jakarta.persistence.*;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "jogadas")
public class Jogada {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "jogo_id", nullable = false)
    private Jogo jogo;

    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @Column(name = "linha")
    private Integer linha;

    @Column(name = "coluna")
    private Integer coluna;

    @Enumerated(EnumType.STRING)
    @Column(name = "tipo_celula")
    private TipoCelula tipoCelula;

    @Column(name = "valor_antes")
    private BigDecimal valorAntes;

    @Column(name = "valor_depois")
    private BigDecimal valorDepois;

    @Column(name = "diamantes_ate_agora")
    private Integer diamantesAteAgora;

    @Column(name = "numero_jogada")
    private Integer numeroJogada;

    @Column(name = "data_jogo")
    private LocalDateTime dataJogo;

    public Jogada() {
    }

    public Jogada(Jogo jogo, User user, Integer linha, Integer coluna,
                  TipoCelula tipoCelula, BigDecimal valorAntes, BigDecimal valorDepois,
                  Integer diamantesAteAgora, Integer numeroJogo) {
        this.jogo = jogo;
        this.user = user;
        this.linha = linha;
        this.coluna = coluna;
        this.tipoCelula = tipoCelula;
        this.valorAntes = valorAntes;
        this.valorDepois = valorDepois;
        this.diamantesAteAgora = diamantesAteAgora;
        this.numeroJogada = numeroJogo;
        this.dataJogo = LocalDateTime.now();
    }

    public Jogada(Jogo jogo, User user, Integer linha, Integer coluna, TipoCelula tipoCelula) {
        this.jogo = jogo;
        this.user = user;
        this.linha = linha;
        this.coluna = coluna;
        this.tipoCelula = tipoCelula;
        this.valorAntes = jogo.getValorAcumulado();
        this.valorDepois = jogo.getValorAcumulado();
        this.diamantesAteAgora = jogo.getDiamantesEncontrados();
        this.numeroJogada = jogo.getJogadasRealizadas();
        this.dataJogo = LocalDateTime.now();
    }


    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
}

